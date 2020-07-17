import random
from collections import deque


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def fisher_yates_shuffle(self, l):
        for i in range(0, len(l)):
            random_index = random.randint(i, len(l) - 1)
            l[random_index], l[i] = l[i], l[random_index]

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Imp 1
        # Add users
        # # use num users
        for user in range(num_users):
            self.add_user(user)

        # Create friendships
        # #make a list with all possible friendships
        friendships = []

        for user in range(1, self.last_id + 1):
            for friend in range(user + 1, num_users + 1):
                friendship = (user, friend)
                friendships.append(friendship)

        # Shuffle the list
        self.fisher_yates_shuffle(friendships)

        # Take as many as we need
        total_friendships = num_users * avg_friendships

        random_friendships = friendships[:total_friendships//2]

        # Add to self.friendships
        for friendship in random_friendships:
            self.add_friendship(friendship[0], friendship[1])

        # Imp 2
        # # Add users
        # for i in range(0, num_users):
        #     self.add_user(f'User {i}')

        # # Create friendships
        #  # Generate all possible friendship combinations
        # possible_friendships = []

        # # Avoid duplicates by ensuring first number is smaller than second
        # for user_id in self.users:
        #     for friend_id in range(user_id + 1, self.last_id + 1):
        #         possible_friendships.append((user_id, friend_id))

        # # Shuffle possible friendships
        # random.shuffle(possible_friendships)

        # # Create friendships for first X pairs of the list
        # # X is determined by: num_users * avg_friendships // 2
        # # Divide by 2 because each add_friendship() makes 2 friendships
        # for i in range(num_users * avg_friendships // 2):
        #     friendship = possible_friendships[i]
        #     self.add_friendship(friendship[0], friendship[1])

    def linear_populate_graph(self, num_users, avg_friendships):
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Add users
        # # use num users
        for user in range(num_users):
            self.add_user(user)

        # linear way
        target_number_friendships = num_users * avg_friendships
        friendships_created = 0

        while friendships_created < target_number_friendships:
            friend_one = random.randint(1, self.last_id)
            friend_two = random.randint(1, self.last_id)

            friendship_was_made = self.add_friendship(friend_one, friend_two)

            if friendship_was_made:
                friendships_created += 2

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.

        Plan: BFT, use dictionary as visited
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        # Imp 1
        q = Queue()
        q.enqueue([user_id])

        # while q isn't empty
        while q.size() > 0:
            # dequeue the current path
            current_path = q.dequeue()

        # grab last vertex from path
            current_user = current_path[-1]

            # if it hasn't been visited
            if current_user not in visited:
                # add to our dictionary
                #### { friend_id: path }
                visited[current_user] = current_path

                friends = self.friendships[current_user]
        # then enqueue PATHS TO each of our neighbors
                for friend in friends:
                    path_to_friend = current_path + [friend]

                    q.enqueue(path_to_friend)

        return visited

        # Imp 2
        # q = deque()
        # q.append((user_id, []))

        # while len(q) > 0:
        #     user, path = q.popleft()

        #     if user not in visited:
        #         path.append(user)
        #         visited[user] = path

        #         for friend in self.friendships[user]:
        #             q.append((friend, path.copy()))

        # return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.linear_populate_graph(10000, 5)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    # print(connections)

# What % of toatal users are in our extended network?

# How many people we know , divided by how many people there are
print(f'{(len(connections) - 1) / 10000 * 100}%')
