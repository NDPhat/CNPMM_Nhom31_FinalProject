package com.example.myapplication.service;
import com.example.myapplication.model.User;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

import retrofit2.Call;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;
import retrofit2.http.Body;
import retrofit2.http.POST;

public interface ApiService {
            Gson gson=new GsonBuilder()
            .setDateFormat("yyyy-MM-dd-HH:mm:ss")
            .create();
    ApiService apiService=new Retrofit.Builder()
            .baseUrl("http://group-31-ccnpmm.me/start/")
            .addConverterFactory(GsonConverterFactory.create(gson))
            .build()
            .create(ApiService.class);


    @POST("signup_function/")
    Call<User> requestRegisterUser(@Body User user);


    @POST("login_function/")
    Call<User> requestLoginUser  (@Body User user);

}
