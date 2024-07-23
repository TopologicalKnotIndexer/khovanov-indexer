# 桥接：https://github.com/TopologicalKnotIndexer/khovanov-solver
import os
DIRNOW = os.path.dirname(os.path.abspath(__file__))
SUBDIR = os.path.join(DIRNOW, "khovanov-solver", "src") # 子包路径


# ======================================== BEGIN IMPORT FROM PATH ======================================== #
import importlib
import json
import sys
def load_module_from_path(path: str, mod_name: str): # 从指定路径导入一个包
    assert os.path.isdir(path)                       # 路径必须存在
    path         = os.path.abspath(path)             # 获得绝对路径
    old_sys_path = json.loads(json.dumps(sys.path))  # 存档旧的 sys.path
    sys.path     = [path] + sys.path                 # 将新的路径加入 sys.path
    mod          = importlib.import_module(mod_name) # 加载指定的包
    sys.path     = old_sys_path                      # 恢复旧的 sys.path
    return mod
# ======================================== END IMPORT FROM PATH ======================================== #

def get_khovanov_by_pd_code(pd_code: list) -> str:
    return load_module_from_path(SUBDIR, "kho_solver").kho_solver(pd_code)

if __name__ == "__main__":
    print(get_khovanov_by_pd_code([[1, 5, 2, 4], [3, 1, 4, 6], [5, 3, 6, 2]]))