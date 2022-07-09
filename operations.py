from sqlalchemy import create_engine
from sqlalchemy.orm import Session,sessionmaker
from database import Users,Hpressure,Lpressure,Heatbeatrate


engine = create_engine(
    "postgresql+psycopg2://des:des@localhost/health", 
    echo=True, pool_size=6, max_overflow=10, encoding='latin1'
)


def create_user(data):
    session = Session(bind=engine)
    c1 = Users(nickname = data['nickname'],
                phone = data['phone'],
                telegram_id = data['telegram_id'])
    session.add(c1)
    session.new
    session.commit()

def create_hpressure(data):
    session = Session(bind=engine)
    hp = Hpressure(user_id = data['user_id'],value = data['value'])
    session.add(hp)
    session.new
    session.commit()

def create_lpressure(data):
    session = Session(bind=engine)
    hp = Lpressure(user_id = data['user_id'],value = data['value'])
    session.add(hp)
    session.new
    session.commit()

def create_heatbeatrate(data):
    session = Session(bind=engine)
    hp = Heatbeatrate(user_id = data['user_id'],value = data['value'])
    session.add(hp)
    session.new
    session.commit()

def get_user(user_id):
    session = Session(bind=engine)
    result = session.query(Users).get(user_id)
    data = { }
    if result:
        data['nickname'] = result.nickname
        data['telegram_id'] = result.telegram_id
        data['phone'] = result.phone
        data['hpressure'] = list(map(lambda x:{
            'data': x.created_on, 'value': x.value
        },result.hpressure))
        data['lpressure'] = list(map(lambda x:{
            'data': x.created_on, 'value': x.value
        },result.lpressure))
        data['heatbeatrate'] = list(map(lambda x:{
            'data': x.created_on, 'value': x.value
        },result.heatbeatrate))

    return data

def get_all_users():
    session = Session(bind=engine)
    result = session.query(Users).all()
    users_list = [item.id for item in result]
    return users_list

