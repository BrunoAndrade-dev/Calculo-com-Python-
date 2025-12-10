import numpy as np 
def calcular_newton(f_num, f_derivada_num, x0, tol, max_iter):
    """
    Executa o Método de Newton sem nenhuma saída (print ou plot).
    Retorna os dados necessários para a visualização no Streamlit.
    """
    X_n = x0
    erros = []
    tabela_dados = [] 
    sucesso = False
    
    for n in range(1, max_iter + 1):
        f_val = f_num(X_n)
        f_derivada_val = f_derivada_num(X_n)

        if abs(f_derivada_val) < 1e-10:
            return tabela_dados, erros, None, f"FALHA: Derivada próxima de zero em x = {X_n:.6f}."

        X_n1 = X_n - f_val / f_derivada_val
        erro = abs(X_n1 - X_n)
        erros.append(erro)
        
        tabela_dados.append({
            'Iteração': n,
            'x_n (Atual)': f"{X_n:.8f}",
            'x_n+1 (Próximo)': f"{X_n1:.8f}",
            'f(x_n)': f"{f_val:.2e}",
            'Erro Absoluto': f"{erro:.2e}"
        })
        
        
        if erro < tol:
            sucesso = True
            break
            
        X_n = X_n1
        
    if sucesso:
        status_msg = f"SUCESSO! Raiz encontrada: x ≈ {X_n1:.8f} após {n} iterações."
        return tabela_dados, erros, X_n1, status_msg
    else:
        status_msg = f"FALHA: O método não convergiu após {max_iter} iterações."
        return tabela_dados, erros, X_n1 if 'X_n1' in locals() else None, status_msg