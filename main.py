from google.cloud import firestore


def item(request):
    """HTTP Cloud Function. Used to interact with item Firestore collection.

    Args:
        request (flask.Request): The request object.
        <http://flask.pocoo.org/docs/1.0/api/#flask.Request>

    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.

    """
    db = firestore.Client()
    collection = db.collection(u'item')
    if request.method == 'GET':
        return get_item(collection, request)
    elif request.method == 'POST':
        payload = request.get_json()
        name = payload.pop('name')
        collection.document(name).set(request.get_json())


def get_item(collection, request):
    """Get an item from the collection using the request.

    Args:
        collection (FirestoreCollection): Previously defined selection.
        request (flask.Request): The request object.

    Returns:
        List<dict>: List of items found.
    """
    item_id = request.path.split('item/')[-1]
    print(item_id)
    if item_id:
        doc = collection.document(item_id)
        return doc.get().to_dict()
    else:
        docs = collection.stream()
    _results = []

    for doc in docs:
        _item = doc.to_dict()
        _item.update({
            'id': doc.id
        })
        _results.append(_item)
    return _results
