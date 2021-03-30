SQL_SEL_TAB_USUARIO = "SELECT * FROM tb_usuario WHERE idt_usuario = {}"

SQL_INS_USU_CANDANGO = "INSERT INTO tb_usuario (cod_level, qtd_exp_atual, url_fto_conta, nme_usuario,eml_usuario,pwd_usuario) values (1, 0, null, '{}', '{}', '{}')"

SQL_SEL_LOGIN_USUARIO = "select tu.id_usuario, tu.eml_usuario, tu.pwd_usuario, tu.nme_usuario, tu.qtd_exp_atual, tu.cod_level from tb_usuario tu "\
                        "where eml_usuario = '{}' and pwd_usuario = '{}';"

SQL_SEL_INFO_USUARIO = "select id_level, qtd_experiencia, nme_level, nme_usuario, qtd_exp_atual from tb_usuario tu " \

