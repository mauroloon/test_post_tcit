import { createSlice, PayloadAction } from '@reduxjs/toolkit';

interface Post {
  id: number;
  name: string;
  description: string;
}

interface PostsState {
  items: Post[];
  searchText: string;
}

const initialState: PostsState = {
  items: [],
  searchText: '',
};

export const postsSlice = createSlice({
  name: 'posts',
  initialState,
  reducers: {
    setPosts: (state, action: PayloadAction<Post[]>) => {
      state.items = action.payload;
    },
    addPost: (state, action: PayloadAction<Post>) => {
      state.items.push(action.payload);
    },
    removePost: (state, action: PayloadAction<number>) => {
      state.items = state.items.filter(post => post.id !== action.payload);
    },
    setSearchText: (state, action: PayloadAction<string>) => {
      state.searchText = action.payload;
    },
  },
});

export const { setPosts, addPost, removePost, setSearchText } = postsSlice.actions;
export default postsSlice.reducer;
