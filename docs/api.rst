Web API
-------

.. http:get:: /api/timeline/post/

   Get list of posts.

   :<header Accept: ``application/json``

   :query int page: a page number within the paginated result set
   :query string search: a search term

   :>header Content-Type: ``application/json``

   :>json int count: total post count
   :>json string next: link to next page
   :>json string previous: link to previous page
   :>json array results: post query results
   :>jsonarr int results[][id]: post id
   :>jsonarr string results[][title]: post title
   :>jsonarr string results[][description]: post description

   :code 200: Success


.. http:get:: /api/timeline/post/(int:post_id)/

   Get details of a post.

   :param int post_id: post id

   :<header Accept: ``application/json``

   :query string search: a search term

   :>header Content-Type: ``application/json``

   :>json int id: post id
   :>json string title: post title
   :>json string description: post description

   :code 200: Success
