import time
import threading


def slepper(n, name):
    print(f"{name}, start working.")
    time.sleep(n)
    print(f"{name}, finish working.")


# t = threading.Thread(target=slepper, args=(2, 'thread'))
# t.start()

thread_list = []
start = time.time()
for _ in range(5):
    t = threading.Thread(target=slepper, args=(2, f'thread_{_}'))
    thread_list.append(t)
    t.start()
    print(f'{t.name} has started.')

for i in thread_list:
    t.join()

end = time.time()
print(f"Time taken: {end-start}")
print(f'All threads have finished their jobs\n')
print('*'*60+'\n')

start = time.time()
for i in range(5):
    print(f'iteration {i} has started')
    slepper(2, i)

end = time.time()

print(f'time taken: {end-start}')