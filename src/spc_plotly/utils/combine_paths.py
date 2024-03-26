def combine_paths(paths):
    """
    Combines one or more overlapping paths into one so that it shows up as a contiguous
        shape on the chart.
        NOTE:
        This function assumes that the paths parameter is sorted; i.e., the first value
        of the first sublist is before the first value of the second sublist, etc, etc.
        This function most likely will not work if, for example, there are 3 paths and
        the first path does not intersect with the second path but DOES intersect with
        the third path. Given how long runs and short runs are calculated, this should
        never be a problem

    Returns:
        list[list[tuple]]: List of lists that each contain a collection of points representing
            a contiguous path
    """

    for i, p in enumerate(paths):
        # Ensure this is not the last path
        if len(paths) > i + 1:
            next_p = paths[i + 1]

            # Convert to sets to take advantage of set operations
            p_set = set(p)
            next_p_set = set(next_p)

            # If sets overlap OR start of next path comes directly after end of current path
            # TODO: the second clause needs to be adjusted. Currently checks if last value of
            #   current path EQUALS first value of next path.
            if len(p_set.intersection(next_p_set)) > 0 or p[len(p) - 1] == next_p[0]:
                # Get union of two paths, convert to list, and sort
                c_path = sorted(list(p_set.union(next_p_set)))
                # Remove two paths from the current list
                paths.remove(p)
                paths.remove(next_p)
                # Insert combined path back into list
                paths.insert(0, c_path)
                # Re-enter function with updated list of paths
                combine_paths(paths)
            else:
                pass
        else:
            break

    return paths
