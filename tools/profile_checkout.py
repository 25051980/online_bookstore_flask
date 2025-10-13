import cProfile, pstats
from io import StringIO
from app import app
def run_flow():
    with app.test_client() as c:
        c.get("/")
if __name__ == "__main__":
    pr=cProfile.Profile(); pr.enable(); run_flow(); pr.disable()
    s=StringIO(); p=pstats.Stats(pr, stream=s).sort_stats(pstats.SortKey.CUMULATIVE)
    p.print_stats(40); print(s.getvalue())
