# Make a list called print_jobs containing several documents to print
# (e.g., "report", "invoice", "resume"). Create an empty list called
# finished_jobs. Loop through print_jobs, and for each document print
# a message like "Printing report...". Move each printed document to
# finished_jobs. After all jobs are done, print a message listing everything
# in finished_jobs.

print_jobs = ["report", "invoice", "resume"]

finished_jobs = []

while print_jobs:
    job = print_jobs.pop()
    print(f"Printing {job} ...")
    finished_jobs.append(job)

print("\n---Finished jobs---")
for job in finished_jobs:
    print(f" -{job}")
