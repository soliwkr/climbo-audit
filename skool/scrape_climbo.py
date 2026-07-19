#!/usr/bin/env python3
"""
Scrape Climbo Skool community data: members, posts, leaderboard, top post comments.

Key findings from API investigation:
- Posts: pageProps.postTrees[].post.metadata contains title, content, comments count, upvotes
- Members: pageProps.users[].metadata.spData has JSON with pts, lv, role
- Comments: Only returned when User-Agent is a bot (triggers withComments=true server-side)
- Leaderboard: Limited to top 5 by the API (30-day window)
- Post pagination: 33 on page 1, 30 on subsequent pages, up to page 32
- Member pagination: 30 per page via ?p=N
"""

import json
import time
import urllib.request
import urllib.parse
import sys

AUTH_COOKIE = "auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE4MTUzMTAxNTcsImlhdCI6MTc4Mzc3NDE1NywidXNlcl9pZCI6ImZiMWRiZTA2MjE0MjQxZGVhNmY2ODg5Mjg4NDI4NjJhIn0.2kGcWMEEP2uJIVMVKk8BdCqsepmLOZEg94K15ISsiZc"
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
BOT_USER_AGENT = "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
BUILD_ID = "1784312549998"
BASE_URL = f"https://www.skool.com/_next/data/{BUILD_ID}/climbo"

OUTPUT_DIR = "/home/soliwkr/Work/climbo-audit/skool"

DELAY = 1.0  # seconds between requests


def fetch(url, use_bot_ua=False):
    """Fetch a URL with auth and return parsed JSON."""
    req = urllib.request.Request(url)
    req.add_header("Cookie", AUTH_COOKIE)
    req.add_header("User-Agent", BOT_USER_AGENT if use_bot_ua else USER_AGENT)
    req.add_header("Accept", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read().decode("utf-8")
            return json.loads(data)
    except Exception as e:
        print(f"  ERROR fetching {url}: {e}", file=sys.stderr)
        return None


def extract_member(user):
    """Extract useful fields from a user object.

    Structure: user has id, name, metadata with bio, location, links, spData, etc.
    """
    metadata = user.get("metadata", {}) or {}

    # Parse spData JSON string
    sp_data = {}
    sp_data_str = metadata.get("spData")
    if sp_data_str:
        try:
            sp_data = json.loads(sp_data_str) if isinstance(sp_data_str, str) else sp_data_str
        except (json.JSONDecodeError, TypeError):
            pass

    result = {
        "id": user.get("id"),
        "name": user.get("name"),
        "bio": metadata.get("bio", ""),
        "location": metadata.get("location", ""),
        "website": metadata.get("linkWebsite", ""),
        "facebook": metadata.get("linkFacebook", ""),
        "instagram": metadata.get("linkInstagram", ""),
        "linkedin": metadata.get("linkLinkedin", ""),
        "twitter": metadata.get("linkTwitter", ""),
        "youtube": metadata.get("linkYoutube", ""),
        "profilePic": metadata.get("pictureProfile", ""),
        "points": sp_data.get("pts"),
        "level": sp_data.get("lv"),
        "role": sp_data.get("role"),
        "pointsCurrentLevel": sp_data.get("pcl"),
        "pointsNextLevel": sp_data.get("pnl"),
        "createdAt": user.get("createdAt") or user.get("created_at"),
        "updatedAt": user.get("updatedAt") or user.get("updated_at"),
    }
    return result


def extract_post(post_tree):
    """Extract useful fields from a postTree object.

    Structure: postTree.post has id, name (slug), metadata (title, content, comments, upvotes, etc.),
    createdAt, updatedAt, groupId, userId, postType, rootId, labelId, user.
    """
    post = post_tree.get("post", post_tree)
    metadata = post.get("metadata", {}) or {}
    user_info = post.get("user", {}) or {}

    # Parse contributors if present
    contributors = []
    contributors_str = metadata.get("contributors")
    if contributors_str:
        try:
            contributors = json.loads(contributors_str) if isinstance(contributors_str, str) else contributors_str
        except (json.JSONDecodeError, TypeError):
            pass

    result = {
        "id": post.get("id"),
        "slug": post.get("name"),  # 'name' field is the URL slug
        "title": metadata.get("title", ""),
        "content": metadata.get("content", ""),
        "commentsCount": metadata.get("comments", 0),
        "upvotes": metadata.get("upvotes", 0),
        "pinned": metadata.get("pinned", 0),
        "authorId": post.get("userId"),
        "authorName": user_info.get("name", ""),
        "authorFirstName": user_info.get("first_name", ""),
        "authorLastName": user_info.get("last_name", ""),
        "createdAt": post.get("createdAt") or post.get("created_at"),
        "updatedAt": post.get("updatedAt") or post.get("updated_at"),
        "labelId": post.get("labelId"),
        "labels": metadata.get("labels", ""),
        "postType": post.get("postType") or post.get("post_type"),
        "imagePreview": metadata.get("imagePreview", ""),
        "videoIds": metadata.get("videoIds", ""),
        "contributorsCount": len(contributors),
    }
    return result


def scrape_members():
    """Scrape all member pages."""
    print("=== SCRAPING MEMBERS ===")
    all_members = []
    page = 1
    max_pages = 35  # safety limit

    while page <= max_pages:
        if page == 1:
            url = f"{BASE_URL}/-/members.json"
        else:
            url = f"{BASE_URL}/-/members.json?p={page}"

        print(f"  Fetching members page {page}...")
        data = fetch(url)

        if data is None:
            print(f"  FAILED page {page}, skipping")
            time.sleep(DELAY)
            page += 1
            continue

        page_props = data.get("pageProps", {})
        users = page_props.get("users", [])

        if not users:
            print(f"  No users found on page {page}, stopping")
            break

        for user in users:
            all_members.append(extract_member(user))

        print(f"  Got {len(users)} members (total so far: {len(all_members)})")

        if len(users) < 30:
            print(f"  Last page reached")
            break

        page += 1
        time.sleep(DELAY)

    print(f"\nTotal members scraped: {len(all_members)}")
    with open(f"{OUTPUT_DIR}/members-full.json", "w") as f:
        json.dump(all_members, f, indent=2, ensure_ascii=False)
    print(f"Saved to {OUTPUT_DIR}/members-full.json")
    return all_members


def scrape_posts():
    """Scrape all posts from community feed."""
    print("\n=== SCRAPING POSTS ===")
    all_posts = []
    page = 1
    max_pages = 40  # safety limit

    while page <= max_pages:
        if page == 1:
            url = f"{BASE_URL}.json"
        else:
            url = f"{BASE_URL}.json?p={page}"

        print(f"  Fetching posts page {page}...")
        data = fetch(url)

        if data is None:
            print(f"  FAILED page {page}, skipping")
            page += 1
            time.sleep(DELAY)
            continue

        page_props = data.get("pageProps", {})
        post_trees = page_props.get("postTrees", [])
        total = page_props.get("total", "?")

        if not post_trees:
            print(f"  No posts found on page {page}, stopping (total reported: {total})")
            break

        for pt in post_trees:
            all_posts.append(extract_post(pt))

        print(f"  Got {len(post_trees)} posts (total so far: {len(all_posts)}, API total: {total})")

        page += 1
        time.sleep(DELAY)

    print(f"\nTotal posts scraped: {len(all_posts)}")
    with open(f"{OUTPUT_DIR}/posts-full.json", "w") as f:
        json.dump(all_posts, f, indent=2, ensure_ascii=False)
    print(f"Saved to {OUTPUT_DIR}/posts-full.json")
    return all_posts


def scrape_leaderboard():
    """Scrape leaderboard data.

    Note: Skool API returns max 5 users for the 30-day leaderboard.
    We also extract leaderboard-like data from the members (who have points).
    """
    print("\n=== SCRAPING LEADERBOARD ===")
    url = f"{BASE_URL}.json?t=leaderboard"
    print(f"  Fetching leaderboard...")
    data = fetch(url)

    if data is None:
        print("  FAILED to fetch leaderboard")
        return {}

    page_props = data.get("pageProps", {})
    leaderboards_data = page_props.get("leaderboardsData", {})
    users = leaderboards_data.get("users", [])

    # Extract and clean leaderboard user data
    cleaned_users = []
    for entry in users:
        user = entry.get("user", {})
        metadata = user.get("metadata", {}) or {}
        sp_data = {}
        sp_data_str = metadata.get("spData")
        if sp_data_str:
            try:
                sp_data = json.loads(sp_data_str) if isinstance(sp_data_str, str) else sp_data_str
            except:
                pass

        cleaned_users.append({
            "userId": entry.get("userId"),
            "name": user.get("name"),
            "bio": metadata.get("bio", ""),
            "location": metadata.get("location", ""),
            "website": metadata.get("linkWebsite", ""),
            "profilePic": metadata.get("pictureProfile", ""),
            "points": sp_data.get("pts"),
            "level": sp_data.get("lv"),
            "role": sp_data.get("role"),
        })

    result = {
        "type": leaderboards_data.get("type"),
        "updatedAt": leaderboards_data.get("updatedAt"),
        "limit": leaderboards_data.get("limit"),
        "users": cleaned_users,
    }

    print(f"\nLeaderboard: {len(cleaned_users)} entries (type: {result['type']})")
    with open(f"{OUTPUT_DIR}/leaderboard-full.json", "w") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"Saved to {OUTPUT_DIR}/leaderboard-full.json")
    return result


def scrape_top_post_comments(all_posts):
    """Scrape full comment trees for top 20 most-commented posts.

    Uses bot User-Agent to trigger server-side comment inclusion (withComments=true).
    Comments appear as postTree.children[] in the response.
    """
    print("\n=== SCRAPING TOP POST COMMENTS ===")

    # Sort posts by comments count
    posts_with_comments = [p for p in all_posts if p.get("commentsCount") and p.get("commentsCount") > 0]
    posts_with_comments.sort(key=lambda x: x.get("commentsCount", 0), reverse=True)

    top_posts = posts_with_comments[:20]
    print(f"  Top {len(top_posts)} posts by comment count:")
    for i, p in enumerate(top_posts):
        print(f"    {i+1}. [{p.get('commentsCount', 0)} comments] {p.get('title', 'untitled')[:60]}")

    detailed_posts = []
    for i, post in enumerate(top_posts):
        slug = post.get("slug")
        if not slug:
            print(f"  Skipping post {i+1} - no slug")
            continue

        # Use bot UA to get comments included in SSR response
        url = f"{BASE_URL}/{slug}.json"
        print(f"  Fetching post {i+1}/{len(top_posts)}: {slug}...")
        data = fetch(url, use_bot_ua=True)

        if data is None:
            print(f"    FAILED, skipping")
            time.sleep(DELAY)
            continue

        page_props = data.get("pageProps", {})
        post_tree = page_props.get("postTree", {})

        # Extract the post and its comment children
        post_data = post_tree.get("post", {})
        post_meta = post_data.get("metadata", {}) or {}
        children = post_tree.get("children", [])

        # Process each comment/child
        comments_cleaned = []
        for child in children:
            child_post = child.get("post", {})
            child_meta = child_post.get("metadata", {}) or {}
            child_user = child_post.get("user", {}) or {}

            comment = {
                "id": child_post.get("id"),
                "content": child_meta.get("content", ""),
                "upvotes": child_meta.get("upvotes", 0),
                "pinned": child_meta.get("pinned", 0),
                "authorId": child_post.get("userId") or child_post.get("user_id"),
                "authorName": child_user.get("name", ""),
                "authorFirstName": child_user.get("first_name", ""),
                "authorLastName": child_user.get("last_name", ""),
                "createdAt": child_post.get("createdAt") or child_post.get("created_at"),
                "updatedAt": child_post.get("updatedAt") or child_post.get("updated_at"),
            }

            # Check for nested replies (children of children)
            sub_children = child.get("children", [])
            if sub_children:
                replies = []
                for sub in sub_children:
                    sub_post = sub.get("post", {})
                    sub_meta = sub_post.get("metadata", {}) or {}
                    sub_user = sub_post.get("user", {}) or {}
                    replies.append({
                        "id": sub_post.get("id"),
                        "content": sub_meta.get("content", ""),
                        "upvotes": sub_meta.get("upvotes", 0),
                        "authorId": sub_post.get("userId") or sub_post.get("user_id"),
                        "authorName": sub_user.get("name", ""),
                        "authorFirstName": sub_user.get("first_name", ""),
                        "authorLastName": sub_user.get("last_name", ""),
                        "createdAt": sub_post.get("createdAt") or sub_post.get("created_at"),
                    })
                comment["replies"] = replies

            comments_cleaned.append(comment)

        post_detail = {
            "slug": slug,
            "title": post_meta.get("title", post.get("title", "")),
            "content": post_meta.get("content", ""),
            "commentsCountReported": post.get("commentsCount"),
            "commentsCountActual": len(comments_cleaned),
            "upvotes": post_meta.get("upvotes", 0),
            "authorId": post_data.get("userId"),
            "createdAt": post_data.get("createdAt"),
            "comments": comments_cleaned,
        }

        total_with_replies = len(comments_cleaned) + sum(len(c.get("replies", [])) for c in comments_cleaned)
        print(f"    Got {len(comments_cleaned)} top-level comments ({total_with_replies} total with replies)")
        detailed_posts.append(post_detail)
        time.sleep(DELAY)

    print(f"\nTotal detailed posts with comments: {len(detailed_posts)}")
    with open(f"{OUTPUT_DIR}/top-posts-comments.json", "w") as f:
        json.dump(detailed_posts, f, indent=2, ensure_ascii=False)
    print(f"Saved to {OUTPUT_DIR}/top-posts-comments.json")
    return detailed_posts


def main():
    print("Starting Climbo Skool community scrape...")
    print(f"Build ID: {BUILD_ID}")
    print(f"Output directory: {OUTPUT_DIR}")
    print()

    # 1. Scrape members
    members = scrape_members()

    # 2. Scrape posts
    posts = scrape_posts()

    # 3. Scrape leaderboard
    leaderboard = scrape_leaderboard()

    # 4. Scrape top post comments
    if posts:
        top_comments = scrape_top_post_comments(posts)
    else:
        top_comments = []
        print("\nSkipping top post comments (no posts scraped)")

    # Summary
    print("\n" + "=" * 50)
    print("SCRAPE COMPLETE - SUMMARY")
    print("=" * 50)
    print(f"  Members:     {len(members)}")
    print(f"  Posts:       {len(posts)}")
    print(f"  Leaderboard: {len(leaderboard.get('users', []))} entries")
    print(f"  Top posts:   {len(top_comments)} with full comment trees")


if __name__ == "__main__":
    main()
