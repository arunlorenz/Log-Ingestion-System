import json
from elasticsearch import Elasticsearch

# Create an Elasticsearch client with basic authentication
es = Elasticsearch(
    cloud_id="6de3ad7e9bee47d39c8fcd2ca4c8e8e4:dXMtY2VudHJhbDEuZ2NwLmNsb3VkLmVzLmlvOjQ0MyQ1YjhmMTY3NzY5ZjY0Y2ZhOWRlNDI2MmU3ZTM3OTJmZCQzZDAzMzU0NjAwOWU0OWM5YWY5YzI1N2FjMTZmNDA4Nw==",
    basic_auth=('21eca12@karpagamtech.ac.in', 'ARUNns123@#$')  
)

# Define an HTTP server that listens on port 3000
from http.server import HTTPServer, BaseHTTPRequestHandler

class LogHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        # Parse the incoming JSON data
        content_length = int(self.headers['Content-Length'])
        post_data = json.loads(self.rfile.read(content_length).decode('utf-8'))
        # Extract the relevant fields
        level = post_data['level']
        message = post_data['message']
        resourceId = post_data['resourceId']
        timestamp = post_data['timestamp']
        traceId = post_data['traceId']
        spanId = post_data['spanId']
        commit = post_data['commit']
        metadata = post_data['metadata']
        parentResourceId = metadata['parentResourceId']

        # Create an Elasticsearch document
        doc = {
            'level': level,
            'message': message,
            'resource_id': resourceId,
            'timestamp': timestamp,
            'trace_id': traceId,
            'span_id': spanId,
            'commit': commit,
            'metadata': {
                'parent_resource_id': parentResourceId
            }
        }

        # Index the document in Elasticsearch
        es.index(index='logs', body=doc)
        # Send a response to the client
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({'message': 'Log ingested successfully'}).encode('utf-8'))

# Create and start the HTTP server
httpd = HTTPServer(('localhost', 3000), LogHandler)
httpd.serve_forever()