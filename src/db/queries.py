SQL_SEL_TAB_USUARIO = "SELECT * FROM tb_usuario WHERE idt_usuario = {}"

SQL_INS_USU_CANDANGO = """INSERT INTO tb_usuario (nme_usuario, eml_usuario, pwd_usuario, tlf_usuario, gen_usuario,  
                                                est_usuario, pais_usuario, status_usuario  ) 
                                                values ('{}', '{}', '{}', '{}','{}', '{}','{}','{}')"""

SQL_SEL_LOGIN_USUARIO = "select * from tb_usuario tu "\
                        "where eml_usuario = '{}' and pwd_usuario = '{}' and status_usuario is not false;"

SQL_SEL_USUARIO_POR_ID = "select * from tb_usuario tu "\
                         "where idt_usuario = '{}'"

SQL_SEL_INFO_USUARIO = "select id_level, qtd_experiencia, nme_level, nme_usuario, qtd_exp_atual from tb_usuario tu " \

