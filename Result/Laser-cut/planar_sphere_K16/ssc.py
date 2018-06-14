import math
import copy
import numpy
import json
import io

N =  16
M =  16
V= [0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]

Normal = [ [ 0.600925094015932,0.112969906611128,-0.791281764975168 ], [ -0.774488740434556,0.0300412422523315,-0.631873970585933 ], [ -0.422276197427813,0.616606060600377,-0.664439447291317 ], [ -0.152510316866707,0.152510428898669,-0.976463605223646 ], [ -0.0643631141399058,0.963978468811132,-0.258075378923985 ], [ 0.707682970629073,0.692045070105197,-0.142332125764719 ], [ 0.315238346908906,-0.938293453323528,-0.14223283758805 ], [ -1.53291841650805E-08,-0.73583795655729,-0.677157663834348 ], [ 0.957652473307908,-0.231266880097275,-0.171514928030532 ], [ -0.596743133950564,-0.574298639126454,-0.560427252353383 ], [ -0.450103241730624,-0.886856957636621,0.104363827426462 ], [ 0.591736078832789,-0.499647607986909,-0.632614164274366 ], [ -0.921372767946603,-0.34317055338867,-0.182499845954264 ], [ -0.850860734003739,0.507630603743256,-0.13545176807217 ], [ -0.123595788359686,-0.0959455156368807,-0.98768342049916 ], [ 0.323857668147611,0.558926528134989,-0.763359251551299 ], ]

orderjoint =  {0: {3: [7], 5: [7], 8: [7], 11: [7], 14: [3, 7], 15: [3, 7]}, 1: {}, 2: {}, 3: {14: [0], 15: [0]}, 4: {}, 5: {}, 6: {}, 7: {6: [0], 9: [0], 10: [0], 11: [0], 14: [0]}, 8: {}, 9: {}, 10: {}, 11: {}, 12: {}, 13: {}, 14: {0: [15], 1: [15], 3: [15], 7: [15], 9: [15], 11: [15]}, 15: {0: [14], 2: [14], 3: [14], 4: [14], 5: [14]}}

nojoint =  [[0, 7], [7, 0], [7, 0], [0, 7], [14, 15], [15, 14], [15, 14], [14, 15]]

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
u = 6

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