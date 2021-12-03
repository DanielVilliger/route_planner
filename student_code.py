from queue import PriorityQueue
import math
def distance(intersect_number, intersect_number_0,a_map):
    pair_list=a_map.intersections[intersect_number]
    pair_list_0=a_map.intersections[intersect_number_0]
    return math.sqrt(math.pow(pair_list[0]-pair_list[0],2)+math.pow(pair_list[1]-pair_list_0[1],2))
#print(map_40.intersections)
def h_nodes(end_node,a_map):
    dict_={}
    for index in range(len(a_map.intersections)):
        dict_[index]=distance(index,end_node,a_map)
    return dict_
def shortest_path(a_map,start,end):
    queue=PriorityQueue()
    prev_link={start: None}
    g_values={start: 0}
    h_values=h_nodes(end,a_map)
    queue.put([h_values[start],start])
    while not queue.empty():
        current_node=queue.get()
        if current_node[1]==end:
            
            return reconstruct(prev_link,end)
        for neighbor in a_map.roads[current_node[1]]:
            g_tent=g_values[current_node[1]]+distance(current_node[1],neighbor,a_map)
            if neighbor not in g_values or g_tent < g_values[neighbor]:
                g_values[neighbor]=g_tent
                f_value=g_tent+h_values[neighbor]
                queue.put([f_value,neighbor])
                prev_link[neighbor]=current_node[1]
    return "Not linked"        
  


def reconstruct(prev_link,end):
    list_=[]
    if None==prev_link[end]:
        return [end]
    if end==None:
        return "Not linked"
    start=prev_link[end]
    list_.append(end)
    list_.append(start)
    while True:
        start=prev_link[start]
        if start==None:
            list_.append(start)
            list_=list_[:-1]
            return list_[::-1]
        list_.append(start)
