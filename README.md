# path_planing
一个路径规划问题，用到了dijkstra和旅行商算法

---

程序文件：
- `DataProcess.py` 处理json文件和dict对象
- `DistanceUtil.py/DistanceCalculator` 该类用来计算边的权值，并写入 edges2.json
- `learnDijstra/demo.py/dijkstra_demo` 该类实现 dijkstra 算法，计算某一点到其他点的最短距离和路径
- `CalShortestPathsForEachPoints.py/my_calculation` 该类计算所有点到其他点的最短距离和路径，将结果存入`shortestpaths.json` 中
- `MatplotlibDemo.py/` 使用 matplotlib 绘制原图形

数据文件：
- `data.json` 录入的记录原始点的信息
- `edges.json` 录入的记录原始的边信息，没有权值
- `edges2.json` 经过计算的边信息，带有权值
- `shortestpaths.json` 记录最终得到的每个路径点到其他路径点的最短距离和路径
