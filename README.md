# Freshdesk Ticket Reader

A Python-based command-line tool that fetches and displays customer support tickets from Freshdesk. This tool provides a quick and efficient way to view recent tickets with detailed information, making it easier to monitor and track customer support activities.

## Features

- 📋 Fetches the 10 most recent tickets from Freshdesk
- 🔍 Displays comprehensive ticket information including:
  - Ticket ID and Subject
  - Status and Priority levels
  - Source (Email, Chat, Phone, etc.)
  - Requester information
  - Assignment details
  - Due dates and Tags
  - Creation and last update timestamps
- 🔒 Secure credentials management using environment variables
- 🎯 Clean and formatted output for easy reading
- ⚡ Fast and efficient API integration

## Prerequisites

- Python 3.6 or higher
- Freshdesk account with API access
- API key from your Freshdesk account

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/freshdesk-ticket-reader.git
cd freshdesk-ticket-reader
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Set up your credentials:
   - Copy the example environment file:
     ```bash
     cp .env.example .env
     ```
   - Edit `.env` and add your Freshdesk credentials:
     ```
     FRESHCHAT_API_KEY=your_api_key_here
     FRESHCHAT_DOMAIN=your_domain_here  # e.g., yourcompany.freshdesk.com
     ```

## Usage

Run the script:
```bash
python fetch_chats.py
```

The output will show the 10 most recent tickets with detailed information for each ticket.

### Understanding the Output

Each ticket display includes:
- 🎫 **Ticket ID**: Unique identifier for the ticket
- 📝 **Subject**: Main topic or title of the ticket
- 📊 **Status**: Current state (Open, Pending, Resolved, etc.)
- 🔥 **Priority**: Importance level (Low, Medium, High, Urgent)
- 📱 **Source**: Where the ticket originated from
- 👤 **Requester**: Customer who created the ticket
- 👨‍💼 **Assigned To**: Agent handling the ticket
- 🏷️ **Tags**: Associated labels
- ⏰ **Timestamps**: Creation and last update times

## Security Considerations

- Never commit the `.env` file to version control
- Keep your API key secure and rotate it regularly
- The `.gitignore` file is configured to exclude sensitive information
- Review code before committing to ensure no credentials are exposed

## Troubleshooting

Common issues and solutions:
1. **Authentication Error**: Verify your API key in the `.env` file
2. **Connection Error**: Check your internet connection and domain name
3. **No Output**: Ensure your account has tickets and proper permissions

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.