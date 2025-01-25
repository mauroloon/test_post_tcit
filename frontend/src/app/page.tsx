'use client'
import { useState, useEffect } from 'react';
import styles from "./page.module.css";
import { Table } from '../components/Table';
import { getPosts, createPost, deletePost } from '../services/postService';

export default function Home() {
  const [searchText, setSearchText] = useState('');
  const [formName, setFormName] = useState('');
  const [formDescription, setFormDescription] = useState('');
  const [posts, setPosts] = useState([]);

  const handleDelete = async (id: number) => {
    try {
      await deletePost(id);
      setPosts(posts.filter(post => post.id !== id));
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const handleCreate = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const newPost = await createPost(formName, formDescription);
      setPosts([...posts, newPost]);
      setFormName('');
      setFormDescription('');
    } catch (error) {
      console.error('Error creating post:', error);
    }
  };

  useEffect(() => {
    getPosts()
      .then(data => setPosts(data))
      .catch(error => console.error('Error fetching posts:', error));
  }, []);

  return (
    <div className={styles.page}>
      <main className={styles.main}>
        <div className={styles.searchSection}>
          <input 
            type="text" 
            value={searchText}
            onChange={(e) => setSearchText(e.target.value)}
            placeholder="Buscar..."
          />
          <button 
            className={styles.button}
            onClick={() => console.log('Buscar:', searchText)}
          >
            Buscar
          </button>
        </div>

        <Table data={posts} onDelete={handleDelete} />

        <form className={styles.form} onSubmit={handleCreate}>
          <input
            type="text"
            value={formName}
            onChange={(e) => setFormName(e.target.value)}
            placeholder="Nombre"
          />
          <input
            type="text"
            value={formDescription}
            onChange={(e) => setFormDescription(e.target.value)}
            placeholder="Descripción"
          />
          <button className={styles.button} type="submit">Crear</button>
        </form>
      </main>
    </div>
  );
}


