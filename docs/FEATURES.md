# Features

## qBittorrent

- Access external web UI for file removal or settings adjustment. Sync with database using the sync button in bot settings.
- Select files from a torrent before or during download using the MLTB file selector (requires Base URL) (task option).
- Seed torrents to a specific ratio and duration (task option).
- Edit global options during runtime via bot settings (global option).

## Aria2c

- Select torrent files before or during download (requires Base URL) (task option).
- Seed torrents to a specific ratio and duration (task option).
- Netrc authentication support (global option).
- Direct link authentication (even with only a username or password) (task option).
- Edit global options during runtime via bot settings (global option).

## Sabnzbd

- Access external web interface for file removal or settings adjustments. Sync with database using the sync button in bot settings.
- Remove files from jobs before or during download using the MLTB file selector (requires Base URL) (task option).
- Edit global options during runtime via bot settings (global option).
- Manage Usenet servers (add/edit/remove).

## Telegram Upload/Download

- Configure split size for uploads (global, user, and task option).
- Use custom thumbnails for uploads (user and task option).
- Add a prefix to leeched filenames (user option).
- Set upload type (document or media) (global, user, and task option).
- Upload to a specific chat (supergroup, channel, private chat, or topic) (global, user, and task option).
- Option for equal split sizes (global and user option).
- Media group support for sending split file parts (global and user option).
- Download restricted Telegram messages using public, private, or supergroup links (task option).
- Choose transfer session (bot or user) for Telegram premium accounts (global, user, and task option).
- Hybrid upload mode using both bot and user sessions based on file size (global, user, and task option).
- Upload with a custom thumbnail layout (global, user, and task option).
- Full topic support for uploads and downloads within groups.

## Google Drive

- Perform operations: download, upload, clone, delete, and count files/folders.
- Search for files and folders within specific Drive folders or TeamDrives.
- Fallback to `token.pickle` authentication when no Service Account is available.
- Utilize a random Service Account for each task to distribute API usage.
- Recursive search support using root or TeamDrive ID (task option).
- Option to prevent duplicate uploads by checking filenames (global and user option).
- Define custom upload destinations (global, user, and task option).
- Choose between `token.pickle` or Service Accounts for authentication, with button support for selection (global, user, and task option).
- Index link support for [Bhadoo's Index](https://gitlab.com/GoogleDriveIndex/Google-Drive-Index/-/blob/master/src/worker.js).

## Rclone

- Transfer (download/upload/clone server-side) with or without random Service Accounts (global and user option).
- Choose config, remote, and path with or without button support (global, user, and task option).
- Set custom flags per task or globally (global, user, and task option).
- File/folder selection via buttons (task option).
- Use `rclone.conf` (global and user option).
- Serve combined remotes as an index (global option).
- Custom upload destinations (global, user, and task option).

## Status

- View download, upload, extract, archive, seed, and clone statuses.
- Unlimited task status pages (global option).
- Interval-based status message updates (global option).
- Navigate through task status pages using next/previous buttons (global and user option).
- Filter task view by status and type if there are more than 30 tasks (global and user option).
- Use step controls for paginating through tasks (global and user option).
- View user-specific task status (manual refresh only).

## yt-dlp

- Interactive quality selection buttons for downloads (task option).
- Set custom `yt-dlp` options (global, user, and task option).
- Support for `.netrc` file authentication (global option).
- Support for `cookies.txt` file authentication (global option).
- Embed original thumbnail in leeched video files.
- Wide audio format support for extraction.

## JDownloader

- Synchronize JDownloader settings with the bot (global option).
- Option to wait for file selection or variant changes before starting a download.
- Support for `.dlc` container files.
- Manage JDownloader settings via its web interface, Android/iOS apps, or browser extensions.

## MongoDB Database

- Stores bot and user settings, including thumbnails and private files (e.g., `token.pickle`, `rclone.conf`).
- Stores RSS feed data and messages for incomplete tasks (for notification after restart).
- Stores JDownloader settings.
- Automatically stores and updates runtime configurations, effectively managing variables similar to those in a static `config.py`.

## Torrent Search

- Search for torrents using various Torrent Search APIs.
- Utilize qBittorrent's plugin system for enhanced and site-specific searches.

## Archives

- Extract split archives, with or without password protection.
- Zip files or folders, with or without password protection, including support for splitting archives during leech operations.
- Uses 7-Zip for extraction, supporting a wide variety of archive types.

## RSS

- Based on [rss-chan](https://github.com/hyPnOtICDo0g/rss-chan).
- RSS feeds (user option).
- Title filters (feed option).
- Edit feeds live: pause, resume, command and filter edits (feed option).
- Sudo controls for user feeds.
- Fully button-based command execution.

## Overall

- Docker support for `amd64`, `arm64/v8`, `arm/v7`.
- Edit runtime variables and overwrite private files (bot/user level).
- Automatic updates on startup and restart via the `UPSTREAM_REPO` variable.
- Telegraph integration (e.g., via [loaderX-bot](https://github.com/SVR666)).
- Initiate Mirror/Leech/Watch/Clone/Count/Delete operations by replying to messages.
- Support for multiple links or files in a single mirror/leech/clone command.
- Set custom names for all download links (excluding torrents); file extensions are required for direct links (except for yt-dlp results) (global and user option).
- Exclude specified file extensions from upload or clone operations (global and user option).
- "View Link" button providing browser access instead of a direct download link for certain outputs.
- Comprehensive queueing system for all tasks (global option).
- Zip multiple links or unzip archives into a single directory (task option).
- Perform bulk downloads from a Telegram TXT file or newline-separated links in a message (task option).
- Join previously split files (task option).
- Generate sample videos and screenshots (task option).
- Cancel ongoing uploads, clones, archives, extractions, splits, or queued tasks (task option).
- Cancel tasks based on specific statuses using interactive buttons (global option).
- Convert video or audio files to a specific format using filters (task option).
- Force-start queued tasks using commands with arguments (task option).
- Support for shell and executor access for advanced operations.
- Manage sudo users for privileged bot commands.
- Save and reuse custom upload paths.
- Rename files before uploading using name substitution patterns.
- Select the use of `rclone.conf` or `token.pickle` for Google Drive operations without needing `mpt:` or `mrcc:` prefixes in basic scenarios.
- Execute custom FFmpeg commands after a download is complete (task option).
- Automatically change media metadata based on configurations.
- Automatically add watermark text to videos or images.
- Customize caption format for uploaded files.

## YouTube Settings

You can configure default settings for your YouTube uploads. Access these via the main settings menu, then select "YouTube".

*   **Default Privacy**: Set your default YouTube upload privacy.
    *   Options: `unlisted`, `public`, `private`
    *   Default: `unlisted`
*   **Default Category**: Set your default YouTube video category ID.
    *   Example: `22` (for People & Blogs)
    *   Default: `22`
*   **Default Tags**: Set your default YouTube tags, separated by commas.
    *   Example: `tag1, my awesome tag, another tag`
    *   Default: `None` (no tags added by default beyond potentially bot-specific ones)
*   **Default Description**: Set your default YouTube video description. The original filename will often be appended.
    *   Default: `Uploaded by Aeon-MLTB.`