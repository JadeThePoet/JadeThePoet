import random
import time

class XAPIClient:
    def __init__(self):
        self.authenticated = False
        self.rate_limit = 50
        self.requests_made = 0

    def authenticate(self):
        # Simulate authentication process
        time.sleep(1)
        self.authenticated = True
        print("Successfully authenticated with X API")

    def post_poem(self, poem):
        if not self.authenticated:
            raise Exception("Not authenticated. Please call authenticate() first.")

        if self.requests_made >= self.rate_limit:
            raise Exception("Rate limit exceeded. Please try again later.")

        # Simulate posting to X
        time.sleep(0.5)
        self.requests_made += 1
        success = random.random() < 0.95  # 95% success rate

        if success:
            print(f"Successfully posted poem to X: {poem[:50]}...")
            return {"id": f"post_{random.randint(1000000, 9999999)}", "success": True}
        else:
            print("Failed to post poem to X. Retrying...")
            return {"success": False}

    def get_engagement_stats(self, post_id):
        if not self.authenticated:
            raise Exception("Not authenticated. Please call authenticate() first.")

        # Simulate getting engagement stats
        time.sleep(0.3)
        return {
            "likes": random.randint(10, 1000),
            "reposts": random.randint(5, 500),
            "comments": random.randint(1, 100)
        }

    def reset_rate_limit(self):
        self.requests_made = 0
        print("Rate limit reset")
