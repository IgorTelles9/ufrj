class FreeTree{
    constructor(){
        this.links = []
    }
    // checks if are there a and b in different pairs
    isThere(a){
        return this.links.some( ([e,_]) => e === a ) || this.links.some( ([_, e]) => e === a)
    }
    // checks cycles
    isItAvaiable(a,b){
        // if there aren't connections
        if (this.links.length === 0) return true

        // checks if a and b already make a pair
        if (this.links.includes([a,b]) || this.links.includes([b,a])) return false

        
        if (this.isThere(a) && this.isThere(b)) throw `Error: the connection (${a}, ${b}) creates a cycle.`
        if (!this.isThere(a) && !this.isThere(b)) throw `Error: the connection (${a}, ${b}) is unconnected from the rest of the tree.`

        return true
    }

    addEdge(a,b){
      if (this.isItAvaiable(a,b))  this.links.push([a,b])
    }

    rootedTree(root){

        // return an array with all links to the node
        const getConnection = node => {
            let connection = []
            if (this.isThere (node)){
                for (let link of this.links){
                    if (link[0] === node) connection.push(link[1])
                    else if (link[1] === node) connection.push(link[0])
                }
            }
            return connection 
        }

        // transforms a map with links into a rooted tree
        const toRT = (data, map) =>
            new RootedTree(data, ...map.get(data)?.map(child => toRT(child, map))??[])


        // all below creates a map with root => [children] 
        let queue = []
        let seen = new Map()
        let tree_map = new Map ()
        
        queue.push(root)

        while (queue.length !== 0){
            seen.set(queue[0],true)
            let connection = getConnection(queue[0])

            if (connection.length !== 0){
                // if the actual node has no connections, we skip it
                let children = []
                for (let i =0; i < connection.length; i++){
                    if (!seen.get(connection[i])){
                        children.push(connection[i])
                        queue.push(connection[i])
                        seen.set(connection[i], true)
                    }
                }
                tree_map.set(queue[0], children) 
            }
            queue.shift()
        }

        return toRT(root, tree_map)     
    }
}

class RootedTree {
    constructor (data, ...descendants) {
      this.data = data;
      this.descendants = descendants;
    }
}

let t = new FreeTree()
t.addEdge(1,2)
t.addEdge(1,3)
t.addEdge(3,4)
t.addEdge(3,5)
t.addEdge(2,7)
t.addEdge(2,8)
rt = t.rootedTree(1)
console.log(rt)