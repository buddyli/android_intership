{
    "status": {
        "code": "0",
        "message": "SUCCESS"
    },
    "page": {
        "ps": "10",
        "pn": "1",
        "pc": "20",
        "rc": "200"
    },
    "data": {
        % if data and 'items' in data:
        "result":${data['items']}
        % else:
        "result":[]
        % endif
    }
}