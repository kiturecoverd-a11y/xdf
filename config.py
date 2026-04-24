"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                     APEX GUARD — HIGH-END DISCORD SECURITY BOT               ║
║                              Configuration Module                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
Professional, feature-loaded, deadly security configuration.
"""

import os

# ─── Core Bot Settings ─────────────────────────────────────────────────────────
class BotConfig:
    """Immutable core configuration."""
    TOKEN = os.getenv("DISCORD_BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
    PREFIX = os.getenv("BOT_PREFIX", "!")
    OWNER_IDS = list(map(int, os.getenv("OWNER_IDS", "0").split(",")))
    
    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_CHANNEL_ID = int(os.getenv("LOG_CHANNEL_ID", "0"))  # Security events channel
    ERROR_CHANNEL_ID = int(os.getenv("ERROR_CHANNEL_ID", "0"))
    
    # Database
    DATABASE_PATH = os.getenv("DATABASE_PATH", "data/security.db")
    
    # Anti-Spam / Raid
    RAID_DETECTION_WINDOW = int(os.getenv("RAID_WINDOW", "10"))       # seconds
    RAID_JOIN_THRESHOLD = int(os.getenv("RAID_THRESHOLD", "10"))      # joins in window
    SPAM_MESSAGE_THRESHOLD = int(os.getenv("SPAM_THRESHOLD", "5"))    # msgs in window
    SPAM_WINDOW = int(os.getenv("SPAM_WINDOW", "5"))                  # seconds
    SPAM_MUTE_DURATION = int(os.getenv("SPAM_MUTE", "300"))           # seconds
    
    # Verification
    VERIFICATION_ROLE_ID = int(os.getenv("VERIF_ROLE_ID", "0"))
    VERIFICATION_CHANNEL_ID = int(os.getenv("VERIF_CHANNEL_ID", "0"))
    CAPTCHA_TIMEOUT = int(os.getenv("CAPTCHA_TIMEOUT", "300"))        # seconds
    
    # Lockdown
    LOCKDOWN_ROLE_OVERRIDE = True  # Override all channel perms for @everyone

# ─── Security Levels ───────────────────────────────────────────────────────────
class SecurityLevel:
    """Escalating security tiers."""
    NORMAL = 0
    ELEVATED = 1   # Increased logging, stricter spam filters
    HIGH = 2       # Auto-mod enabled, verification required
    CRITICAL = 3   # Server lockdown, manual approval for joins
    DEADLY = 4     # Instant action on threats, zero tolerance

# ─── Punishment Tiers ──────────────────────────────────────────────────────────
class Punishment:
    """Configurable punishment escalation."""
    WARN = "warn"
    MUTE = "mute"
    KICK = "kick"
    SOFTBAN = "softban"   # Kick + delete 24h messages
    BAN = "ban"
    INSTABAN = "instaban"

# ─── Whitelist / Blacklist ─────────────────────────────────────────────────────
WHITELISTED_IDS = set()     # User IDs immune to auto-moderation
BLACKLISTED_IDS = set()     # Instant ban on sight
BLACKLISTED_WORDS = [
    "discord.gg/", "discord.com/invite", "@everyone scam",
    "free nitro", "steam gift", "gift card", "csgo skins free"
]
SUSPICIOUS_INVITE_PATTERNS = [
    r"discord\.gg/[a-zA-Z0-9]{2,}",
    r"discord\.com/invite/[a-zA-Z0-9]{2,}",
    r"dsc\.gg/[a-zA-Z0-9]+",
    r"discord\.me/[a-zA-Z0-9]+",
]

# ─── API Keys (Optional) ───────────────────────────────────────────────────────
class APIs:
    """Optional external threat intelligence."""
    VIRUSTOTAL_API = os.getenv("VIRUSTOTAL_API", "")
    IPQUALITYSCORE_API = os.getenv("IPQUALITY_API", "")

# ─── Feature Flags ─────────────────────────────────────────────────────────────
class Features:
    """Toggle high-end modules."""
    ANTI_RAID = True
    ANTI_SPAM = True
    ANTI_PHISHING = True
    ANTI_NSFW = True
    ANTI_MASS_MENTION = True
    ANTI_CAPITALS_FLOOD = True
    ANTI_EMOJI_FLOOD = True
    ANTI_LINK = False           # Strict mode: block all links
    AUTO_DEHOIST = True         # Remove hoisted nicknames
    AUTO_ROLE = True
    CAPTCHA_VERIFICATION = True
    LOGGING_ADVANCED = True
    BACKUP_GUILD = True
    THREAT_INTELLIGENCE = True
    PRESENCE_TRACKING = True
    ALT_DETECTION = True
    TOKEN_LEAK_DETECTION = True
    FILE_SCAN = True

# ─── Cooldowns & Limits ────────────────────────────────────────────────────────
class Limits:
    """Rate limits and thresholds."""
    COMMAND_COOLDOWN = 3        # seconds per user
    MAX_MENTIONS = 5            # per message
    MAX_LINES = 15              # per message
    MAX_ATTACHMENTS = 4         # per message
    MAX_CHARACTERS = 2000       # per message
    MAX_CAPS_PERCENT = 70       # % of message in caps
    MAX_EMOJIS = 8              # per message
    MAX_NEWLINES = 10           # per message
    REPEATED_MESSAGE_LIMIT = 3  # same message count
    URL_SHORTENER_BLOCK = True
