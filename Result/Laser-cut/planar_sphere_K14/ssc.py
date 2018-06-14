import math
import copy
import numpy
import json
import io

N =  14
M =  14
V= [0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]

Normal = [ [ 0.570371690319727,0.193996030843221,-0.798148905216873 ], [ -0.719919386946209,-2.88505214718349E-08,-0.694057689460317 ], [ -0.345842606703045,0.681239506953661,-0.645217502517079 ], [ -0.0605599754060786,0.167584534829369,-0.983995890776399 ], [ 0.0518411653322746,0.879001136674526,-0.473993138454433 ], [ 0.688104900230221,0.698698825880144,-0.195784567810811 ], [ 0.36021322600734,-0.896679370153503,-0.257317972459178 ], [ -0.125177238505915,-0.523545874184125,-0.842751669582928 ], [ 0.957652483923266,-0.231266877236133,-0.171514872617641 ], [ -0.527664110902996,-0.647301214736523,-0.550065199286023 ], [ -0.346349452531297,-0.937946166093596,-0.0172929535243619 ], [ 0.534929077503038,-0.533059558096793,-0.655513836286771 ], [ -0.896079609080679,-0.356341788936491,-0.264692016591659 ], [ -0.83388706575181,0.550371790609802,0.0415120906820777 ], ]

orderjoint =  {0: {3: [4, 7], 4: [7], 5: [4, 7], 8: [7], 11: [7]}, 1: {7: [9], 12: [9]}, 2: {}, 3: {0: [4, 11], 1: [4, 11], 2: [4, 11], 4: [11], 7: [4, 11], 11: [4]}, 4: {0: [3], 2: [3, 13], 3: [0], 5: [0]}, 5: {}, 6: {7: [8], 10: [7, 8], 11: [7, 8]}, 7: {0: [6, 10], 1: [0, 6, 10], 3: [0, 6, 10], 6: [0, 10], 9: [0, 6, 10], 10: [0, 6], 11: [0, 6, 10]}, 8: {0: [6], 11: [6], 5: [6]}, 9: {7: [1], 12: [1]}, 10: {9: [7, 12], 12: [7], 6: [7]}, 11: {0: [3], 7: [3], 8: [3], 6: [3]}, 12: {1: [13], 9: [10, 13], 10: [13]}, 13: {1: [12], 2: [4, 12], 4: [12]}}

nojoint =  [[0, 7], [7, 0], [3, 4], [4, 3], [3, 11], [11, 3], [4, 3], [3, 4], [6, 7], [7, 6], [6, 8], [8, 6], [7, 0], [0, 7], [7, 6], [6, 7], [7, 10], [10, 7], [8, 6], [6, 8], [10, 7], [7, 10], [11, 3], [3, 11], [12, 13], [13, 12], [13, 12], [12, 13]]

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
                            if VectorDotProduct(vec, Normal[w]) > math.sqrt(1) / 3:
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
u = 3

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