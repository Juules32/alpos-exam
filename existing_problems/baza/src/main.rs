use std::{collections::HashMap, io::{self, BufRead}};

fn count_valid_indices(indices: &Vec<usize>, word_index: usize) -> usize {
    indices.partition_point(|&x| x <= word_index)
}

#[derive(Default)]
struct Node {
    children: HashMap<char, Node>,
    word_indices: Vec<usize>,
}

#[derive(Default)]
struct Trie {
    root: Node
}

impl Trie {
    fn insert(&mut self, word: &str, word_index: usize) {
        let mut current = &mut self.root;
        current.word_indices.push(word_index);
        for ch in word.chars() {
            current = current.children.entry(ch).or_insert_with(Node::default);
            current.word_indices.push(word_index);
        }
    }

    fn count_instructions(&mut self, word: &str, word_index: usize) -> usize {
        let mut current = &mut self.root;
        let mut count = count_valid_indices(&current.word_indices, word_index);

        for ch in word.chars() {
            if current.children.len() == 0 {
                break;
            } else {
                match current.children.get_mut(&ch) {
                    Some(node) => {
                        current = node;
                        count += count_valid_indices(&current.word_indices, word_index);
                    },
                    None => break,
                }
            }
        }

        count
    }
}

fn main() {
    let mut trie = Trie::default();
    let mut word_index_map: HashMap<String, usize> = HashMap::new();
    
    let stdin = io::stdin();
    let mut lines = stdin.lock().lines().map(|l| l.unwrap());

    let n = lines.next().unwrap().parse().unwrap();
    for index in 0..n {
        let word = lines.next().unwrap();
        word_index_map.insert(word.clone(), index);
        trie.insert(&word, index);
    }

    let q = lines.next().unwrap().parse().unwrap();
    for _ in 0..q {
        let query = lines.next().unwrap();
        let query_index = match word_index_map.get(&query) {
            Some(index) => *index,
            None => usize::MAX,
        };

        println!("{}", trie.count_instructions(&query, query_index));
    }
}
