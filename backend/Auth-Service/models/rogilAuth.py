from core.database import baseDB
from sqlalchemy import Column, Integer, String,Text, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship

class User(baseDB):
    __tablename__ = 'RGLUSER'
    USCODE = Column(Integer, primary_key=True, autoincrement=True)
    USNAME = Column(String(255), nullable=False)
    USLASTNAME = Column(String(255), nullable=False)
    USEMAIL = Column(String(255), unique=True, nullable=False)
    USPASSWORD = Column(String(60), nullable=False)
    RLCODE = Column(Integer,ForeignKey('RGLROLE.RLCODE'), nullable=False)
    
    role = relationship('Role', back_populates='user')

class Role(baseDB):
    __tablename__= 'RGLROLE'
    RLCODE = Column(Integer, primary_key=True, autoincrement=True)
    RLNAME = Column(String(100), nullable=False)
    RLDESCRIP = Column(Text, nullable=False)

    user = relationship('User', back_populates='role')
    rpRole = relationship('Role_Permission',back_populates='roleRP')

class Permission(baseDB):
    __tablename__= 'RGLPERMISSION'
    PRMSSCODE = Column(Integer, primary_key=True, autoincrement=True)
    PRMSSNAME = Column(String(100), nullable=False)

    pmPermission = relationship('Permission_MenuOption', back_populates='permissionPM')
    rpPermission = relationship('Role_Permission', back_populates='permissionRP')

class MenuOption(baseDB):
    __tablename__='RGLMENUOPTION'
    MNCODE = Column(Integer, primary_key=True, autoincrement=True)
    MNNAME = Column(String(100), nullable=False)
    MNROUTE = Column(String(100), nullable=True)
    MNPARENT = Column(Integer,ForeignKey('RGLMENUOPTION.MNCODE'),nullable=True)
    MNORDER = Column(Integer, nullable=False)

    subMenus = relationship('MenuOption')

    pmMenuOption = relationship('Permission_MenuOption', back_populates='menuOptionPM')

class Permission_MenuOption(baseDB):
    __tablename__='RGLPERMISSION_MENUOPTION'
    PRMSSCODE = Column(Integer, ForeignKey('RGLPERMISSION.PRMSSCODE'), nullable=False)
    MNCODE = Column(Integer, ForeignKey('RGLMENUOPTION.MNCODE'), nullable=False)

    __table_args__=(
        PrimaryKeyConstraint('PRMSSCODE','MNCODE'),
    )

    menuOptionPM = relationship('MenuOption', back_populates='pmMenuOption')
    permissionPM = relationship('Permission', back_populates='pmPermission')  

class Role_Permission(baseDB):
    __tablename__= 'RGLROLE_PERMISSION'
    RLCODE = Column(Integer, ForeignKey('RGLROLE.RLCODE'),nullable=False)
    PRMSSCODE = Column(Integer, ForeignKey('RGLPERMISSION'), nullable=False)
    
    __table_args__=(
        PrimaryKeyConstraint('RLCODE','PRMSSCODE'),
    )

    roleRP = relationship('Role', back_populates='rpRole')
    permissionRP = relationship('Permission', back_populates='rpPermission')

