import cProfile
import pstats as pt
def calculate():
    total=0
    for i in range(1000):
        total+=i
    return total
profiler=cProfile.Profile()
profiler.enable()
calculate()
profiler.disable()
profiler.dump_stats("profile.prof")
stats=pt.Stats("profile.prof")
# stats.sort_stats("cumulative")
stats.print_stats()