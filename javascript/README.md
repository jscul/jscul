**{}**

_insert_ O(1)
_remove_ O(1)
_search_ O(N)
_access_ O(1)

_{}.keys_ O(N)
_{}.values_ O(N)
_{}.entries_ O(N)
_{}.hasOwnProperty_ O(1)

**[]**

_insert_
 - O(1) push
 - O(N) shift
_remove_
 - O(1) pop
 - O(N) unshift
_search_ O(N)
_access_ O(1)

_concat_ O(N)
_slice_ O(N)
_splice_ O(N)
_sort_ O(N * log(N))
_forEach_/_map_/_filter_/_reduce_/_etc_. O(N)
