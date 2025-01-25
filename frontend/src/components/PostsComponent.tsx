import { useState, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { RootState } from '../redux/store';
import { setPosts, addPost, removePost, setSearchText } from '../redux/slices/postsSlice';
import { getPosts, createPost, deletePost } from '../services/postService';
import { Table } from './Table';
import styles from '../app/page.module.css';

export function PostsComponent() {
  const dispatch = useDispatch();
  const posts = useSelector((state: RootState) => state.posts.items);
  const searchText = useSelector((state: RootState) => state.posts.searchText);
  const [formName, setFormName] = useState('');
  const [formDescription, setFormDescription] = useState('');
  const [filteredPosts, setFilteredPosts] = useState(posts);

  /**
   * Elimina un post
   * @param id - ID del post a eliminar
   */
  const handleDelete = async (id: number) => {
    try {
      await deletePost(id);
      dispatch(removePost(id));
    } catch (error) {
      console.error('Error:', error);
    }
  };

  /**
   * Crea un post
   */
  const handleCreate = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const newPost = await createPost(formName, formDescription);
      if (!newPost.id) {
        throw new Error('El nuevo post debe tener un ID');
      }
      dispatch(addPost(newPost));
      setFormName('');
      setFormDescription('');
    } catch (error) {
      console.error('Error creating post:', error);
    }
  };

  const handleSearch = () => {
    const filtered = posts.filter(post => 
      post.name.toLowerCase().includes(searchText.toLowerCase()) ||
      post.description.toLowerCase().includes(searchText.toLowerCase())
    );
    setFilteredPosts(filtered);
  };

  const handleClear = () => {
    dispatch(setSearchText(''));
    setFilteredPosts(posts);
  };

  useEffect(() => {
    getPosts()
      .then(data => dispatch(setPosts(data)))
      .catch(error => console.error('Error fetching posts:', error));
  }, [dispatch]);

  useEffect(() => {
    setFilteredPosts(posts);
  }, [posts]);

  return (
    <div className={styles.page}>
      <main className={styles.main}>
        <div className={styles.searchSection}>
          <input 
            type="text" 
            value={searchText}
            onChange={(e) => dispatch(setSearchText(e.target.value))}
            placeholder="Buscar..."
          />
          <button 
            className={styles.button}
            onClick={handleClear}
          >
            Limpiar
          </button>
          <button 
            className={styles.button}
            onClick={handleSearch}
          >
            Buscar
          </button>
        </div>

        <Table data={filteredPosts} onDelete={handleDelete} />

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
