from django import dispatch

webhook_received = dispatch.Signal(providing_args=['path', 'request_data'])
