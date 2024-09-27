# Daniel has a ball. He wants to find the ball's rebound height,
# which he dropped from height H with an initial velocity V. After
# 12
# the Nth rebound the final velocity of the ball is V ,, Your task is to help him find and return an integer value representing the height to
# 12
# which the ball rebounds after N bounces.
# 15
# Note:
# -
# . H' = H x e2", where H' is the rebound height. H is the initial height, e is
# the coefficient of restitution and is the number of bounces.
# · en = V/V ,, where V is the initial velocity; and Va is the final velociy
# 2 Search
# Specification:
# steger H, representing initial height
# ar V, representing initial velocity
# representing final velocity

def height(h,v,vn):
    return h*(v//vn)**2
