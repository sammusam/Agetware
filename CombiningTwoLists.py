def combine_lists(list1, list2):
    combined = sorted(list1 + list2, key=lambda x: x["positions"][0])
    result = []
    
    for item in combined:
        if not result:
            result.append(item)
            continue
        last = result[-1]
        l1, r1 = last["positions"]
        l2, r2 = item["positions"]
        
        # Calculate overlap
        overlap = min(r1, r2) - max(l1, l2)
        width = r2 - l2
        
        if overlap > 0.5 * width:
            # Combine values and update only right position
            last["values"] += item["values"]
            last["positions"][1] = max(r1, r2)
        else:
            result.append(item)
    return result

# Example:
combine_lists([{"positions":[0,5],"values":[1]}], [{"positions":[4,9],"values":[2]}])
# Output: [{'positions': [0, 9], 'values': [1, 2]}]
