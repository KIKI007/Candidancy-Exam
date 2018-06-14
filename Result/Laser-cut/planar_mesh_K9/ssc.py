import math
import copy
import numpy
import json
import io

N =  9
M =  9
V= [0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0]

Normal = [ [ 0,-1,0 ], [ 1,0,0 ], [ 0,1,0 ], [ -1,0,0 ], [ 0,0,1 ], [ 0,0.499722453489577,0.866185586048601 ], [ 0.707106781186547,0,-0.707106781186547 ], [ -6.94120665425974E-17,-0.499722453489577,0.866185586048601 ], [ 0.707106781186548,-5.66642342460875E-17,0.707106781186547 ], ]

#orderjoint =  {0: {1: [6, 8], 3: [6, 8], 4: [1, 3, 5, 6, 8], 5: [6, 8], 6: [1, 4, 8], 8: [1, 5, 6]}, 1: {0: [5, 7], 2: [5, 7], 4: [0, 2, 5, 6, 7], 5: [2, 6, 7], 6: [0, 2, 4, 5, 7], 7: [0, 5, 6]}, 2: {1: [6, 8], 3: [6, 8], 4: [1, 3, 6, 7, 8], 6: [1, 4, 8], 7: [6, 8], 8: [1, 6, 7]}, 3: {0: [5, 7], 2: [5, 7], 4: [0, 2, 5, 7, 8], 5: [2, 7, 8], 7: [0, 5, 8], 8: [5, 7]}, 4: {}, 5: {0: [3, 7], 1: [3, 7], 3: [7], 6: [1, 3, 7], 7: [0, 1, 3, 6, 8], 8: [0, 1, 3, 6, 7]}, 6: {0: [8], 1: [0, 8], 2: [0, 8], 5: [0, 1, 2, 7, 8], 7: [0, 1, 5, 8], 8: [0, 1, 2, 5, 7]}, 7: {1: [3, 5], 2: [1, 3, 5], 3: [1, 5], 5: [1, 2, 3, 6, 8], 6: [1, 3, 5], 8: [1, 2, 3, 5, 6]}, 8: {0: [2, 6], 2: [0, 6], 3: [0, 2, 6], 5: [0, 2, 3, 6, 7], 6: [0, 2], 7: [0, 2, 3, 5, 6]}}
orderjoint = {}
for i in range(N):
    orderjoint[i] = {}

nojoint =  [[0, 6], [6, 0], [0, 8], [8, 0], [1, 5], [5, 1], [1, 7], [7, 1], [2, 6], [6, 2], [2, 8], [8, 2], [3, 5], [5, 3], [3, 7], [7, 3], [5, 1], [1, 5], [5, 3], [3, 5], [5, 7], [7, 5], [6, 0], [0, 6], [6, 2], [2, 6], [6, 8], [8, 6], [7, 1], [1, 7], [7, 3], [3, 7], [7, 5], [5, 7], [8, 0], [0, 8], [8, 2], [2, 8], [8, 6], [6, 8]]
center = [ [ 7.50000000000001,-26,7.50000000000001 ], [ 15,-13,7.5 ], [ 7.50000000000001,0,7.50000000000001 ], [ 0,-13,7.5 ], [ 7.5,-13,0 ], [ 7.5,-22.295,12.8625 ], [ 12.8625,-13,12.8625 ], [ 7.5,-3.70500000000001,12.8625 ], [ 2.1375,-13,12.8625 ], ]
def strongly_connected_components_tree(vertices, edges):
    identified = set()
    stack = []
    index = {}
    lowlink = {}

    def dfs(v):
        index[v] = len(stack)
        stack.append(v)
        lowlink[v] = index[v]

        for w in edges[v]:
            if w not in index:
                # For Python >= 3.3, replace with "yield from dfs(w)"
                for scc in dfs(w):
                    yield scc
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif w not in identified:
                lowlink[v] = min(lowlink[v], lowlink[w])

        if lowlink[v] == index[v]:
            scc = set(stack[index[v]:])
            del stack[index[v]:]
            identified.update(scc)
            yield scc

    for v in vertices:
        if v not in index:
            # For Python >= 3.3, replace with "yield from dfs(v)"
            for scc in dfs(v):
                yield scc


def has_joint(u, v):
    if u == v:
        return False
    return bool(V[u * M + v])


def get_order(visited, id):
    if visited.get(id) != None:
        return visited[id]
    else:
        return len(visited)


def is_interlocking(joint_graph, visited, vec, num_vertices):
    vertices = range(num_vertices + 1)
    edges = {}

    for id in range(num_vertices + 1):
        edges[id] = []

    for id in range(N):
        u = get_order(visited, id)
        for jd, edgevec in joint_graph[id].items():
            if VectorDotProduct(edgevec, vec) > -0.95:
                v = get_order(visited, jd)
                if v not in edges[u]:
                    edges[u].append(v)
    for scc in strongly_connected_components_tree(vertices, edges):
        #print scc
        if (0 in scc) and (len(scc) > 1 and len(scc) < num_vertices):
            return False
        if len(scc) == 1 and list(scc)[0] != 0 and num_vertices > 1:
            return False
    return True


def delete_u_from_graph(u, graph):
    graph[u] = []
    for key, value in graph.items():
        if u in value:
            graph[key].remove(u)


def is_graph_connected(graph, num_non_empty_vertices):
    vertices = range(N)
    for scc in strongly_connected_components_tree(vertices, graph):
        if len(scc) == 1:
            if graph[list(scc)[0]] != []:
                return False
        elif len(scc) < num_non_empty_vertices:
            return False
    return True


def is_able_create_joint(visited, joint_graph, u, v):
    if [u, v] in nojoint:
        return False
    for w in visited:
        if has_joint(u, w) and u != w and v != w:
            # print u, v, w, orderjoint[u]
            if joint_graph[w].get(u) == None:
                if orderjoint[u].get(w) != None:
                    if v in orderjoint[u][w]:
                        return False
    return True

def VectorCrossProduct(a, b):
    return numpy.cross(a, b)

def VectorDotProduct(a, b):
    return numpy.dot(a, b)

def VectorScale(a, r):
    b = a.copy()
    b[0] *= r
    b[1] *= r
    b[2] *= r
    return b

def VectorUnitize(a):
    len = math.sqrt(a[0] * a[0] + a[1] * a[1]+ a[2]* a[2])
    return VectorScale(a, 1.0 / len)

def create_joint(u, visited, joint_graph, connected_graph, joint, step, move):
    #print visited
    print u, step
    if step == N - 1:
        global input
        global graph
        global order
        global disvec
        visited[u] = step
        input = joint
        graph = joint_graph
        order = range(N)
        for v, index in visited.items():
            order[index] = v
        disvec = move
        disvec[u] = numpy.array([0,0,0]);
        return True
        ##copy
    c_gh = copy.deepcopy(connected_graph)
    delete_u_from_graph(u, c_gh)
    candidates = []

    ## compute candidates:
    for v in range(N):
        if has_joint(u, v) and visited.get(v) == None:
            cc_gh = copy.deepcopy(c_gh)
            delete_u_from_graph(v, cc_gh)
            if is_graph_connected(cc_gh, N - step - 2):
                candidates.append(v)

    if candidates == []:
        return False

    ## add part
    new_visited = copy.deepcopy(visited)
    new_visited[u] = step

    # print(u, candidates)
    for v in range(N):
        if (is_able_create_joint(visited, joint_graph, u, v) == False):
            continue
        if has_joint(u, v) and visited.get(v) == None:
            for sign in range(-1, 3, 2):
                ## find direction
                new_jt_gh = copy.deepcopy(joint_graph)
                new_move = copy.deepcopy(move)
                new_jt = copy.deepcopy(joint)
                vec = VectorCrossProduct(Normal[u], Normal[v])
                vec = VectorScale(vec, sign)
                vec = VectorUnitize(vec)
                new_move[u] = VectorScale(vec, -1);

                ## create joints
                for w in range(N):
                    if has_joint(u, w):
                        if visited.get(w) == None:
                            if (is_able_create_joint(visited, joint_graph, w, u) == False):
                                new_jt.append([w, u, 2])
                                continue

                            #Tenon Joint
                            sgn = VectorDotProduct(center[w], Normal[w]) - VectorDotProduct(center[u], Normal[w])
                            normalw = numpy.array([Normal[w][0], Normal[w][1], Normal[w][2]])
                            if sgn < 0:
                                normalw = VectorScale(normalw, -1)

                            if VectorDotProduct(vec, normalw) > math.sqrt(1) / 2:
                                new_jt_gh[u][w] = vec
                                new_jt_gh[w][u] = VectorScale(vec, -1)

                                new_jt.append([u, w, 1, vec[0], vec[1], vec[2]])
                                continue

                            #Halve Joint
                            edge_dir = VectorCrossProduct(Normal[u], Normal[w])
                            edge_dir = VectorUnitize(edge_dir)
                            edge_angle = VectorDotProduct(edge_dir, vec)
                            if edge_angle > 0.999:
                                new_jt_gh[u][w] = vec
                                new_jt_gh[w][u] = VectorScale(vec, -1)

                                new_jt.append([u, w, 0, True])
                            elif edge_angle < -0.999:
                                new_jt_gh[u][w] = vec
                                new_jt_gh[w][u] = VectorScale(vec, -1)

                                new_jt.append([u, w, 0, False])
                            else:
                                #Non Joint
                                new_jt.append([w, u, 2])
                        elif joint_graph[w].get(u) != None:
                            if (is_able_create_joint(visited, joint_graph, w, u) == False):
                                return False

                ## check interlocking
                if (is_interlocking(new_jt_gh, new_visited, vec, step + 1)):
                    for cand in candidates:
                        if create_joint(cand, new_visited, new_jt_gh, c_gh, new_jt, step + 1, new_move):
                            return True


c_gh = {}
jt_gh = {}
visited = {}
jt = []
move = {}

for id in range(N):
    jt_gh[id] = {}

for id in range(N):
    c_gh[id] = []
    for jd in range(N):
        if has_joint(id, jd):
            c_gh[id].append(jd)


for u in [4]:
    if create_joint(u, visited, jt_gh, c_gh, jt, 0, move):
        print 'found'
        animation = "Objects " + str(N) + "\n"
        for i in range(N):
            animation += "part_" + str(i) + ".obj "
        animation += "\n\n"
        for u in order:
            vec = disvec[u]
            vec = VectorScale(vec, 2)
            animation += "Begin Action " + str(180) + "\n"
            animation += "Move id " + str(u + 1) + " [" + str(vec[0]) + "," + str(vec[1]) + "," + str(vec[2]) + "]\n"
            animation += "End\n\n"

        with open("/Users/ziqwang/Desktop/WorkSpace/planar_mesh/data.txt", "w") as data_file:
            json.dump(input, data_file)

        with open("/Users/ziqwang/Desktop/WorkSpace/planar_mesh/animation.motion.txt", "w") as animate_file:
            animate_file.write(animation)

        exit

    else:
        print 'fail'
        input = []
        exit