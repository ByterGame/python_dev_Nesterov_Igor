from faker import Faker
import uuid
from datetime import datetime
from models.author_db_models import Author, Blog, Post, db1
from models.logs_db_models import SpaceType, EventType, Logs, db2


def generate_authors(n=10):
    fake = Faker()
    authors = []
    for _ in range(n):
        author = Author.create(
            id=uuid.uuid4(),
            login=fake.user_name(),
            email=fake.email()
        )
        authors.append(author)
    return authors


def generate_blogs(authors, n=5):
    fake = Faker()
    blogs = []
    for _ in range(n):
        blog = Blog.create(
            id=uuid.uuid4(),
            owner=fake.random.choice(authors),
            name=fake.sentence(nb_words=4),
            description=fake.text()
        )
        blogs.append(blog)
    return blogs


def generate_posts(authors, blogs, n=20):
    fake = Faker()
    posts = []
    for _ in range(n):
        post = Post.create(
            id=uuid.uuid4(),
            header=fake.sentence(nb_words=6),
            text=fake.text(),
            author=fake.random.choice(authors),
            blog=fake.random.choice(blogs)
        )
        posts.append(post)
    return posts


def generate_logs(posts, n=30):
    fake = Faker()
    space_types = [SpaceType.create(type=t) for t in ["global", "log", "post"]]
    event_types = [EventType.create(type=e, post_info=fake.random.choice(posts)) for e in ["login", "comment", "create_post", "delete_post", "logout"]]
    
    for _ in range(n):
        Logs.create(
            id=uuid.uuid4(),
            datetime=fake.date_time_this_year(),
            user_login=fake.user_name(),
            space_type_id=fake.random.choice(space_types),
            event_type_id=fake.random.choice(event_types)
        )


def main():
    authors = generate_authors(10)
    print(f"Generated {len(authors)} authors")

    blogs = generate_blogs(authors, 5)
    print(f"Generated {len(blogs)} blogs")

    posts = generate_posts(authors, blogs, 20)
    print(f"Generated {len(posts)} posts")

    generate_logs(posts, 30)
    print("Logs generated")

    print("Data generation complete.")


if __name__ == "__main__":
    main()
