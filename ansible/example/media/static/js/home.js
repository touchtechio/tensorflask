/*
 * JavaScript file for the application to demonstrate
 * using the API
 */

// Create the namespace instance
let ns = {};

var stringTruncate = function(str, length){
  var dots = str.length > length ? '...' : '';
  return str.substring(0, length)+dots;
};


// Create the model instance
ns.model = (function() {
    'use strict';

    let $event_pump = $('body');

    // Return the API
    return {
        read: function() {
            let ajax_options = {
                type: 'GET',
                url: '/media/api/media',
                accepts: 'application/json',
                dataType: 'json'
            };
            $.ajax(ajax_options)
            .done(function(data) {
                $event_pump.trigger('model_read_success', [data]);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        },
        create: function(media) {
            let ajax_options = {
                type: 'POST',
                url: '/media/api/media',
                accepts: 'application/json',
                contentType: 'application/json',
                dataType: 'json',
                data: JSON.stringify(media)
            };
            $.ajax(ajax_options)
            .done(function(data) {
                $event_pump.trigger('model_create_success', [data]);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        },
        update: function(media) {
            let ajax_options = {
                type: 'PUT',
                url: '/media/api/media/' + media.guid,
                accepts: 'application/json',
                contentType: 'application/json',
                dataType: 'json',
                data: JSON.stringify(media)
            };
            $.ajax(ajax_options)
            .done(function(data) {
                $event_pump.trigger('model_update_success', [data]);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        },
        delete: function(guid) {
            let ajax_options = {
                type: 'DELETE',
                url: '/media/api/media/' + guid,
                accepts: 'application/json',
                contentType: 'plain/text'
            };
            $.ajax(ajax_options)
            .done(function(data) {
                $event_pump.trigger('model_delete_success', [data]);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        }
    };
}());

// Create the view instance
ns.view = (function() {
    'use strict';

    let $guid = $('#guid'),
        $uri = $('#uri'),
        $filename = $('#filename');

    // return the API
    return {
        reset: function() {
            $guid.val('');
            $filename.val('');
            $uri.val('').focus();
        },
        update_editor: function(media) {
            $guid.val(media.guid);
            $filename.val(media.filename);
            $uri.val(media.uri).focus();
        },
        build_table: function(media) {
            let rows = ''

            // clear the table
            $('.media table > tbody').empty();

            // did we get a media array?
            if (media) {
                for (let i=0, l=media.length; i < l; i++) {
                    rows += `<tr data-media-id="${media[i].guid}">
                        <td class="guid">${stringTruncate(media[i].guid, 20)}</td>
                        <td class="filename"><a href="${media[i].uri}">${media[i].filename}</a></td>
                        <td class="uri">${media[i].uri}</td>
                        <td>${media[i].timestamp}</td>
                    </tr>`;
                }
                $('table > tbody').append(rows);
            }
        },
        error: function(error_msg) {
            $('.error')
                .text(error_msg)
                .css('visibility', 'visible');
            setTimeout(function() {
                $('.error').css('visibility', 'hidden');
            }, 3000)
        }
    };
}());

// Create the controller
ns.controller = (function(m, v) {
    'use strict';

    let model = m,
        view = v,
        $event_pump = $('body'),
        $guid = $('#guid'),
        $uri = $('#uri'),
        $filename = $('#filename');

    // Get the data from the model after the controller is done initializing
    setTimeout(function() {
        model.read();
    }, 100)

    // Validate input
    function validate(uri, filename) {
        return uri !== "" && filename !== "";
    }

    // Create our event handlers
    $('#create').click(function(e) {
        let uri = $uri.val(),
            guid = $guid.val(),
            filename = $filename.val();

        e.preventDefault();

        if (validate(uri, filename)) {
            model.create({
                'guid': guid,
                'uri': uri,
                'filename': filename
            })
        } else {
            alert('Problem with media input');
        }
    });

    $('#update').click(function(e) {
        let guid = $guid.val(),
            uri = $uri.val(),
            filename = $filename.val();

        e.preventDefault();

        if (validate(uri, filename)) {
            model.update({
                guid: guid,
                uri: uri,
                filename: filename
            })
        } else {
            alert('Problem with media input');
        }
        e.preventDefault();
    });

    $('#delete').click(function(e) {
        let guid = $guid.val();

        e.preventDefault();

        if (validate('placeholder', filename)) {
            model.delete(guid)
        } else {
            alert('Problem with uri filename input');
        }
        e.preventDefault();
    });

    $('#reset').click(function() {
        view.reset();
    })

    $('table > tbody').on('dblclick', 'tr', function(e) {
        let $target = $(e.target),
            guid,
            uri,
            filename;

        guid = $target
            .parent()
            .attr('data-media-id');

        uri = $target
            .parent()
            .find('td.uri')
            .text();

        filename = $target
            .parent()
            .find('td.filename')
            .text();

        view.update_editor({
            guid: guid,
            uri: uri,
            filename: filename,
        });
    });

    // Handle the model events
    $event_pump.on('model_read_success', function(e, data) {
        view.build_table(data);
        view.reset();
    });

    $event_pump.on('model_create_success', function(e, data) {
        model.read();
    });

    $event_pump.on('model_update_success', function(e, data) {
        model.read();
    });

    $event_pump.on('model_delete_success', function(e, data) {
        model.read();
    });

    $event_pump.on('model_error', function(e, xhr, textStatus, errorThrown) {
        let error_msg = textStatus + ': ' + errorThrown + ' - ' + xhr.responseJSON.detail;
        view.error(error_msg);
        console.log(error_msg);
    })
}(ns.model, ns.view));


