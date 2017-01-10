# cache_container
## What is it?
> A cache container is a iterator 
> which can dump class from memory to disk,
> and read it from disk later.

## Usage
~~~
 from cache_container import CacheContainer
 my_cache_container = CacheContainer(some_iterator_if_u_want)
 my_cache_container.dump(obj)
 obj = my_cache_container.load()
 for obj in my_cache_container:
    do_something(obj)
~~~

