from models.logs_db_models import Logs, SpaceType, EventType
from models.author_db_models import Post, Author, Blog
from peewee import fn, Case


def get_comments_info(user_login):
    logs_query = (Logs
                  .select(
                      Logs.user_login.alias('user_login'),
                      Logs.info_about_post.alias('post_id')
                  )
                  .join(EventType, on=(Logs.event_type_id == EventType.id))
                  .where((EventType.type == 'comment')))

    logs_data = list(logs_query.dicts())

    post_ids = [log['post_id'] for log in logs_data if log['post_id'] is not None]
    if not post_ids:
        return [] 

    posts_query = (Post
                   .select(
                       Post.id.alias('post_id'),
                       Post.header.alias('post_header'),
                       Author.login.alias('author_login')
                   )
                   .join(Author, on=(Post.author == Author.id))
                   .where(Post.id.in_(post_ids)))

    posts_data = list(posts_query.dicts().execute())
    
    posts_dict = {post['post_id']: post for post in posts_data}
    final_data = []
    
    for log in logs_data:
        if log['user_login'] != user_login:
            continue
        print(log['post_id'])
        post_info = posts_dict.get(log['post_id'], {'post_header': 'Unknown', 'author_login': 'Unknown'})
        final_data.append({
            'user_login': log['user_login'],
            'post_header': post_info['post_header'],
            'author_login': post_info['author_login']
        })

    return final_data 


def get_general_info(user_login):        
    query = (Logs
    .select(
        fn.strftime('%Y-%m-%d', Logs.datetime).alias('date'),
        fn.SUM(Case(None, [(EventType.type == 'login', 1)], 0)).alias('login_count'),
        fn.SUM(Case(None, [(EventType.type == 'logout', 1)], 0)).alias('logout_count'),
        fn.SUM(Case(None, [(EventType.type.in_(['comment', 'create_post', 'delete_post']), 1)], 0)).alias('blog_actions_count')
    )
    .join(EventType, on=(Logs.event_type_id == EventType.id))
    .where(Logs.user_login == user_login)
    .group_by(fn.strftime('%Y-%m-%d', Logs.datetime))
    .dicts()
    )

    result = [
        {
            "date": log['date'], 
            "login_count": log['login_count'],
            "logout_count": log['logout_count'],
            "blog_actions_count": log['blog_actions_count']
        }
        for log in query  
    ]    
    return result

