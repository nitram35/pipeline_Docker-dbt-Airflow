-- It's a jinja, look at it
{% set film_title = 'Whiplash' %}

SELECT *
FROM {{ref('films')}}
WHERE title = '{{film_title}}'