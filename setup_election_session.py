def setup_election_session_demo():
    print("--- Election Session Setup (Admin) ---")
    
    # Details from your screenshot
    election_title = "General Election 2025"
    constituency = "All (National)"
    start_date = "01 / 06 / 2025 08:00"
    end_date = "01 / 06 / 2025 18:00"
    candidates = ["Ahmed Hassan", "Mira Chowdhury", "Rafiq Islam"]

    # Session Settings
    max_votes_per_voter = 1
    allow_proxy = "No"
    live_results = "After Close"
    audit_log = "Enabled"
    backup = "Auto"

    print(f"Creating Session: {election_title}")
    print(f"Constituency: {constituency}")
    print(f"Timing: {start_date} to {end_date}")
    print(f"Candidates: {', '.join(candidates)}")
    
    print("\nSession Settings Configured:")
    print(f" - Max Votes: {max_votes_per_voter}")
    print(f" - Allow Proxy: {allow_proxy}")
    print(f" - Live Results: {live_results}")
    print(f" - Audit Log: {audit_log}")
    print(f" - Backup: {backup}")
    
    print("\n[✔] Session Created & Locked")
    print("[!] Session changes require re-approval")

if __name__ == "__main__":
    setup_election_session_demo()