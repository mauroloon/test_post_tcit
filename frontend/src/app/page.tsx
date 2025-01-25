'use client'
import { Provider } from 'react-redux';
import { store } from '../redux/store';
import { PostsComponent } from '@/components/PostsComponent';

export default function Home() {
  return (
    <Provider store={store}>
      <PostsComponent />
    </Provider>
  );
}


