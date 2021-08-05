class RootedTree {
    constructor (data, ...descendants) {
      this.data = data;
      this.descendants = descendants;
    }
}


class FreeTree{
    constructor(){
        // Relation between key and value: a key is the value's parent. 
        this.children = [];
        this.parents = [];
    }
    // checks unconnected nodes
    isThere(a){
        if (this.parents.includes(a) || this.children.includes(a)){
            return true
        }
        return false 
    }
    // checks cycles
    areThere(a,b){
        const both_child = this.children.includes(a) && this.children.includes(b)
        const both_parent = this.parents.includes(a) && this.parents.includes(b)
        const child_parent = false
            //(this.parents.includes(a) || this.parents.includes(b)) &&
            //(this.children.includes(a) || this.children.includes(b))

        if (both_child || both_parent || child_parent)  return true
        return false 
    }

    addEdge(a,b){
      if (this.isThere(a) || this.isThere(b) || this.parents.length === 0){
        if (!this.areThere(a,b)){
          this.parents.push(a)
          this.children.push(b)
        } else throw "Error: you can't create a cycle"
       } else throw "Error: you can't create an unconnected node"
    }

    rootedTree(root){
        let children = [...this.children]
        let parents = [...this.parents]
        let temp_node;

        let rt1 = new RootedTree(root)

        // eu utilizei dois arrays para organizar os pares conectados
        // dado um par [x,y], o array parents recebe x e children
        function tooRootedTree(rt){ // a função já recebe uma árvore
            let size = children.length // == parents.length
            if (children.includes(rt.data) || parents.includes(rt.data)){ // se o data da arvore esta em algum dos arrays, significa que há conexões
                for (let i = 0; i < size; i++){ // percorre o array
                    // como são dois arrays, preciso de dois ifs
                    if (children[i] === rt.data) {  
                        // identificou rt.data no array children: significa que o nó conectado a ele está em parent, no mesmo índice
                        temp_node = new RootedTree(parents[i]) // cria uma árvore com o nó conectado
                        parents.splice(i,1) // exclui o par dos arrays
                        children.splice(i,1)
                        console.log (rt.descendants)
                        // adiciona a arvore criada aos descedants do rt atual
                        return rt.descendants.push(tooRootedTree(temp_node)) // mas chama a funcao novamente, agora com a arvore criada como rt                     
                    }
                    if (parents[i] === rt.data) {
                        temp_node = new RootedTree(children[i])
                        parents.splice(i,1)
                        children.splice(i,1)
                        return rt.descendants.push(tooRootedTree(temp_node))
                    }
                }
            }else{ // se o data da nao arvore esta em algum dos arrays, significa que nao há conexões
                return rt.descendants = null 
            } 
        }  
    }
}

let t = new FreeTree();
for (let [a,b] of [[4,6],[4,5],[2,4],[1,2],[1,3],[3,7],[4,8],[1,9]]) {
  t.addEdge(a,b)
}
console.log(t.rootedTree(1))
