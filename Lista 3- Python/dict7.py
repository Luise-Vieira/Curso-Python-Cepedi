alunos = {
"Ana": {"Matemática", "Física"},
"Bruno": {"Geografia", "História"},
"Carla": {"Matemática", "História"}
}
atividadesanaecarla=alunos["Ana"].union(alunos["Carla"])
print(atividadesanaecarla)