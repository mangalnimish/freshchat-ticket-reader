import os
import requests
from datetime import datetime
from dotenv import load_dotenv

def load_config():
    """Load configuration from environment variables"""
    load_dotenv()
    return {
        'api_key': os.getenv('FRESHCHAT_API_KEY'),
        'domain': os.getenv('FRESHCHAT_DOMAIN')
    }

def fetch_recent_tickets(config, limit=10):
    """Fetch recent tickets from Freshdesk"""
    auth = (config["api_key"], 'X')  # Freshdesk uses API key as username and 'X' as password
    headers = {
        'Content-Type': 'application/json'
    }
    
    url = f"https://{config['domain']}/api/v2/tickets"
    params = {
        'per_page': limit,
        'order_by': 'updated_at',
        'order_type': 'desc'
    }
    
    try:
        response = requests.get(url, auth=auth, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        print(f"Successfully fetched {len(data)} tickets")
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching tickets: {e}")
        return None

def format_ticket_data(tickets):
    """Format ticket data for display"""
    if not tickets:
        return
    
    status_map = {
        2: "Open",
        3: "Pending",
        4: "Resolved",
        5: "Closed",
        6: "Waiting on Customer",
        7: "Waiting on Third Party",
        8: "Waiting on Engineering",
        9: "Cancelled",
        10: "In Progress"
    }
    
    priority_map = {
        1: "Low",
        2: "Medium",
        3: "High",
        4: "Urgent"
    }

    source_map = {
        1: "Email",
        2: "Portal",
        3: "Phone",
        4: "Forum",
        5: "Twitter",
        6: "Facebook",
        7: "Chat",
        8: "Mobihelp",
        9: "Feedback Widget",
        10: "Outbound Email"
    }
    
    for ticket in tickets:
        print("\n" + "=" * 70)
        print(f"Ticket ID: {ticket['id']}")
        print(f"Subject: {ticket['subject']}")
        
        # Status and Priority
        print(f"Status: {status_map.get(ticket['status'], str(ticket['status']))}")
        print(f"Priority: {priority_map.get(ticket['priority'], str(ticket['priority']))}")
        
        # Source of ticket
        print(f"Source: {source_map.get(ticket['source'], 'Unknown')}")
        
        # Requester details
        if 'requester' in ticket:
            print(f"Requester: {ticket['requester'].get('name', 'N/A')} ({ticket['requester'].get('email', 'N/A')})")
        
        # Assignee details
        if ticket.get('responder_id'):
            print(f"Assigned To: {ticket.get('responder_name', 'N/A')}")
        
        # Group assignment
        if ticket.get('group_id'):
            print(f"Group: {ticket.get('group_name', 'N/A')}")
        
        # Due date if available
        if ticket.get('due_by'):
            print(f"Due By: {ticket['due_by']}")
        
        # Tags
        if ticket.get('tags'):
            print(f"Tags: {', '.join(ticket['tags'])}")
        
        # Description (truncated)
        if ticket.get('description_text'):
            desc = ticket['description_text']
            if len(desc) > 100:
                desc = desc[:97] + "..."
            print(f"\nDescription: {desc}")
        
        # Timestamps
        print(f"\nCreated At: {ticket['created_at']}")
        print(f"Updated At: {ticket['updated_at']}")
        print("=" * 70)

def main():
    config = load_config()
    
    if not config['api_key'] or not config['domain']:
        print("Error: Missing API key or domain in environment variables")
        return
    
    tickets = fetch_recent_tickets(config)
    if tickets:
        format_ticket_data(tickets)

if __name__ == "__main__":
    main()
