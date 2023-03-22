import React, { useState, useEffect } from 'react';
import { View, Text, FlatList, TouchableOpacity } from 'react-native';

export default function CategoryScreen({ navigation }) {
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    const fetchCategories = async () => {
      try {
        console.log("useffect of categories")
        const response = await fetch('http://127.0.0.1:8000/RecipeApp/categories/');
        console.log(response)
        const data = await response.json();
        setCategories(data);
      } catch (error) {
        console.error(error);
      }
    };

    fetchCategories();
  }, []);

  const handleCategoryPress = async (category) => {
    try {
      const response = await fetch(``);
      const data = await response.json();
      navigation.navigate('Recipes', { recipes: data });
    } catch (error) {
      console.error(error);
    }
  };

  const renderCategoryItem = ({ item }) => (
    <TouchableOpacity onPress={() => handleCategoryPress(item)}>
      <Text>{item.categoryName}</Text>
    </TouchableOpacity>
  );

  return (
    <View>
      <Text>Hiii</Text>
      <FlatList
        data={categories}
        renderItem={renderCategoryItem}
        keyExtractor={(item) => item.id.toString()}
      />
    </View>
  );
}
