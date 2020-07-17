q = deque()
        q.append((user_id, []))

        while len(q) > 0:
            user, path = q.popleft()

            if user not in visited:
                path.append(user)
                visited[user] = path

                for friend in self.friendships[user]:
                    q.append((friend, path.copy()))