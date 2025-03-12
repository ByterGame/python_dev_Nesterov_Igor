from faker import Faker
import uuid
from datetime import datetime
from models.author_db_models import Author, Blog, Post, db1
from models.logs_db_models import SpaceType, EventType, Logs, db2


def generate_authors(n=1000):
    fake = Faker()
    authors = []
    for _ in range(n):               
        author = Author.create(
            id=uuid.uuid4(),
            login=f"{fake.user_name()}{fake.random_int(1000, 9999)}",
            email=f"{fake.email()}{fake.random_int(1000, 9999)}"
        )
        authors.append(author)
    return authors


def generate_blogs(authors, n=2000):
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


def generate_posts(authors, blogs, n=2000):
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


def generate_logs(posts, n=5000):
    fake = Faker()
    space_types = [SpaceType.create(type=t) for t in ["global", "blog", "post"]]
    event_types = {e: EventType.get_or_create(type=e)[0] for e in ["login", "comment", "create_post", "delete_post", "logout"]}
    usernames = list(set(fake.user_name() for _ in range(200)))[:100]
    for _ in range(n):
        event_type = fake.random.choice(list(event_types.keys()))        
        Logs.create(
            id=uuid.uuid4(),
            datetime=fake.date_time_this_year(),
            user_login=usernames[fake.random_int(min=0, max=99)],
            space_type_id=fake.random.choice(space_types),
            event_type_id=event_types[event_type],
            info_about_post=str(fake.random.choice(posts).id).replace('-','') if event_type == "comment" else None
        )


def main():
    authors = generate_authors()
    print(f"Generated {len(authors)} authors")

    blogs = generate_blogs(authors)
    print(f"Generated {len(blogs)} blogs")

    posts = generate_posts(authors, blogs)
    print(f"Generated {len(posts)} posts")

    generate_logs(posts)
    print("Logs generated")

    print("Data generation complete.")


if __name__ == "__main__":
    main()
