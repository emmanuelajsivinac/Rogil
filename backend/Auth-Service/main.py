from core.database import handlerDB
from models.rogilAuth import User, Role, Permission, MenuOption, Permission_MenuOption, Role_Permission
from sqlalchemy.orm import Session
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from schemas.user import AuthUser

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.post('/login')
async def authUser(user: AuthUser):
    print(f'{user.email}{user.password}')
    db: Session = handlerDB.get_connection()
    dbUser = db.query(User).filter(User.USEMAIL == user.email).first()
    USCODE = dbUser.USCODE
    USNAME = dbUser.USNAME
    USLASTNAME = dbUser.USLASTNAME
    dbRolename = (
        db.query(Role.RLNAME)
        .join(Role_Permission, Role.RLCODE == Role_Permission.RLCODE)
        .join(User, User.RLCODE == Role_Permission.RLCODE)
        .filter(User.USCODE == USCODE)
        .first()
    )
    ROLENAME = dbRolename[0]

    db.close()
    return{'token':'hola','uscode':USCODE,'name':USNAME,'lastname':USLASTNAME,'role':ROLENAME}

@app.get('/loadMenu/{uscode}')
async def loadMenu(uscode: int):
    db : Session = handlerDB.get_connection()
    parent_menus = (
                        db.query(
                            MenuOption.MNCODE,
                            MenuOption.MNNAME,
                            MenuOption.MNROUTE,
                            MenuOption.MNPARENT,
                            MenuOption.MNORDER,
                        )
                        .join(Permission_MenuOption, MenuOption.MNCODE == Permission_MenuOption.MNCODE)
                        .join(Role_Permission, Permission_MenuOption.PRMSSCODE == Role_Permission.PRMSSCODE)
                        .join(User, User.RLCODE == Role_Permission.RLCODE)
                        .filter(User.USCODE == uscode)
                        .all()
    )
    #Error al no convertirlo a lista
    menu_list = []
    for menu in parent_menus:
        menu_list.append({
            'code':menu[0],
            'name':menu[1],
            'route':menu[2],
            'parent':menu[3],
            'order':menu[4],
        })

    return{'menus':menu_list}



