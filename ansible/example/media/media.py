from datetime import datetime
import uuid
# 3rd party modules
from flask import (
    make_response,
    abort
)


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Data to serve with our API
MEDIA = {
    "guid_media_999": {
        "guid": "guid_media_999",
        "filename": "exploratorium.mp4",
        "uri": "https://s3-us-west-2.amazonaws.com/content.touchtech.io/media/VID_20180803_201053.mp4",
        "timestamp": get_timestamp()
    },
    "guid_media_998": {
        "guid": "guid_media_998",
        "filename": "spider-robots.MOV",
        "uri": "https://s3-us-west-2.amazonaws.com/content.touchtech.io/media/spider-robots.MOV",
        "timestamp": get_timestamp()
    },
    "guid_media_997": {
        "guid": "guid_media_997",
        "filename": "GagaDmxRing.mp4",
        "uri": "http://contentai.intel.com/m/GagaDmxRing.mp4",
        "timestamp": get_timestamp()
    },
    "guid_media_996": {
        "guid": "guid_media_996",
        "filename": "7C2A1862-roto-before.mov",
        "uri": "https://s3-us-west-2.amazonaws.com/content.touchtech.io/media/7C2A1862-roto-before-vlc.webm",
        "timestamp": get_timestamp()
    }
}


# Create a handler for our read (GET) media list
def read_all():
    """
    This function responds to a request for /media/api/media
    with the complete lists of media

    :return:        sorted list of media
    """
    # Create the list of media from our data
    return [MEDIA[key] for key in sorted(MEDIA.keys())]


# Create a handler for our read (GET) media
def read_one(guid):
    """
    This function responds to a request for /media/api/media/{guid}

    :param guid:    guid of media record to find
    :return:        media record
    """

    # does the media exist
    if guid in MEDIA:
        media = MEDIA.get(guid)

    # otherwise, nope, not found error
    else:
        abort(404, 'Media with given guid {guid} not found'.format(guid=guid))

    return media


# Create a handler for our read (GET) media
def create(media):
    """
    This function responds to a request for /media/api/media/{guid}

    :param media:   media record to create
    :return:        201 on success, 406 on media record already exists
    """

    guid = media.get('guid', None)
    filename = media.get('filename', None)
    uri = media.get('uri', None)

    if '' is guid or guid is None:
        guid = 'guid_media_'+str(uuid.uuid4())

    # if the the media does not exist, CREATE
    if guid not in MEDIA and guid is not None:
        MEDIA[guid] = {
            'guid': guid,
            'filename': filename,
            'uri': uri,
            'timestamp': get_timestamp()
        }

        # call server-side functions
        #

        return make_response('{guid} successfully create for {filename}'.format(guid=guid, filename=filename), 201)

    # otherwise, it exists, so error
    else:
        abort(406, 'media already exists with given guid {guid}'.format(guid=guid))


def update(guid, media):
    """
    This function updates an existing media in the media structure
    :param guid:   guid of media to update in the media structure
    :param media:  media to update
    :return:        updated media structure
    """
    # Does the media exist in media list?
    if guid in MEDIA:
        MEDIA[guid]['filename'] = media.get('filename')
        MEDIA[guid]['uri'] = media.get('uri')
        MEDIA[guid]['timestamp'] = get_timestamp()

        return MEDIA[guid]

    # otherwise, nope, that's an error
    else:
        abort(404, 'Media with guid {guid} not found'.format(
            guid=guid))


def delete(guid):
    """
    This function deletes a media from the media structure
    :param media:   guid of media to delete
    :return:        200 on successful delete, 404 if not found
    """
    # Does the media to delete exist?
    if guid in MEDIA:
        del MEDIA[guid]
        return make_response('{guid} successfully deleted'.format(
            guid=guid), 200)

    # Otherwise, nope, media to delete not found
    else:
        abort(404, 'Media with guid  {guid} not found'.format(
            guid=guid))
