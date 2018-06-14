import math
import copy
import numpy
import json
import io

N =  10
M =  10
V= [0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0]

Normal = [ [ 0.594643885390069,0.149168035496055,-0.790030092309432 ], [ -0.89008557928329,0.0635346223094361,-0.451343564615613 ], [ -0.583347054705639,0.704157617473723,-0.40480645192485 ], [ -0.137561982862385,0.138965762361009,-0.980696292316022 ], [ 0.0983017305286655,0.88490292205924,-0.455284074294378 ], [ 0.688104891406186,0.698698810859556,-0.195784652427926 ], [ 0.234239272871537,-0.933939050773936,-0.269981133570651 ], [ -0.0260741656558461,-0.532740244969868,-0.845877041463354 ], [ 0.8975215031596,-0.310130166478164,-0.313487529586679 ], [ -0.740002910180164,-0.609476396649286,-0.284489393215794 ], ]

orderjoint =  {0: {3: [4, 7], 4: [5, 7], 5: [4, 7], 7: [4], 8: [4, 5, 7]}, 1: {2: [7], 3: [7], 9: [7]}, 2: {1: [3], 4: [3]}, 3: {0: [2, 4, 9], 1: [2, 4, 9], 2: [4, 9], 4: [2, 9], 7: [2, 4, 9], 9: [2, 4]}, 4: {0: [3], 2: [0, 3], 3: [0], 5: [0, 3]}, 5: {0: [8], 8: [0], 4: [0, 8]}, 6: {7: [9], 8: [9]}, 7: {0: [1, 8], 1: [0, 8], 3: [0, 1, 8], 6: [0, 1, 8], 8: [0, 1], 9: [0, 1, 8]}, 8: {0: [5, 7], 7: [5], 5: [7], 6: [5, 7]}, 9: {7: [3, 6], 1: [3, 6, 7], 3: [6], 6: [3]}}

nojoint =  [[0, 4], [4, 0], [0, 7], [7, 0], [1, 7], [7, 1], [2, 3], [3, 2], [3, 2], [2, 3], [3, 4], [4, 3], [3, 9], [9, 3], [4, 0], [0, 4], [4, 3], [3, 4], [5, 8], [8, 5], [6, 9], [9, 6], [7, 0], [0, 7], [7, 1], [1, 7], [7, 8], [8, 7], [8, 5], [5, 8], [8, 7], [7, 8], [9, 3], [3, 9], [9, 6], [6, 9]]
order = []

disvec = {}

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
            if VectorDotProduct(edgevec, vec) > -0.9:
                v = get_order(visited, jd)
                if v not in edges[u]:
                    edges[u].append(v)
    for scc in strongly_connected_components_tree(vertices, edges):
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
                            if VectorDotProduct(vec, Normal[w]) > math.sqrt(1) / 2:
                                new_jt_gh[u][w] = vec
                                new_jt_gh[w][u] = VectorScale(vec, -1)

                                new_jt.append([u, w, 1, vec[0], vec[1], vec[2]])
                                continue
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
u = 0

for id in range(N):
    jt_gh[id] = {}

for id in range(N):
    c_gh[id] = []
    for jd in range(N):
        if has_joint(id, jd):
            c_gh[id].append(jd)


if create_joint(u, visited, jt_gh, c_gh, jt, 0, move):
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

    with open("data.txt", "w") as data_file:
        json.dump(input, data_file)

    with open("animation.motion.txt", "w") as animate_file:
        animate_file.write(animation)

else:
    input = []