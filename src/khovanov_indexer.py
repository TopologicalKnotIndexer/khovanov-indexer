# 根据 PD_CODE 确定 khovanov 同调
# 再根据 khovanov 同调确定扭结名称

from get_khovanov_by_pd_code  import get_khovanov_by_pd_code
from get_knotname_by_khovanov import get_knotname_by_khovanov

def khovanov_indexer(pd_code: list) -> list[str]: # 给定 PD_CODE，确定扭结名称
    khovanov = get_khovanov_by_pd_code(pd_code)
    knotname_list = get_knotname_by_khovanov(khovanov)
    return knotname_list

if __name__ == "__main__": # 测试
    print(khovanov_indexer([[1, 5, 2, 4], [3, 1, 4, 6], [5, 3, 6, 2]]))